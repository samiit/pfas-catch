"""Main file rendering the APIs"""

from pathlib import Path
from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse


from audio_utils import get_text_from_whisper
from src.utils import get_filename, get_molecules, get_smiles

app = FastAPI()


@app.get("/")
def get_pfas_match_root():
    """Base API for PFAS to Adsorber match"""
    return {"PFAS": "DETA-adsorber"}


@app.post("/smiles")
async def get_smiles_from_text(text: str):
    """Get the SMILES representation from the given text description of the molecule"""
    molecule_names = get_molecules(text)
    return [get_smiles(molecule_name) for molecule_name in molecule_names]


@app.post("/render2d")
async def get_2d_render_from_smiles(smiles: str) -> FileResponse:
    """Returns an image from a give smiles text"""
    filename = get_filename(smiles) + ".jpg"  # Assuming the images are in PNG format
    file_path = Path("images") / filename
    return FileResponse(file_path, media_type="image/jpg")


@app.post("/render3d")
async def get_3d_render_from_smiles(smiles: str) -> FileResponse:
    """Returns a 3D renderable mol2 file from a given smiles text"""
    filename = get_filename(smiles) + "_gaff.mol2"
    file_path = Path("images") / filename
    return FileResponse(file_path, media_type="text/mol2")


@app.post("/text2imagefiles")
async def get_images_from_text(text: str):
    """Returns a list of image files from the text description of the molecule"""
    molecule_names = get_molecules(text)
    images = []
    mol2_files = []
    for molecule_name in molecule_names:
        smiles = get_smiles(molecule_name)
        filename = get_filename(smiles) + ".jpg"
        file_path = Path("images") / filename
        images.append(FileResponse(file_path, media_type="image/jpg"))

        mol2_filename = get_filename(smiles) + "_gaff.mol2"
        mol2_file_path = Path("images") / mol2_filename
        mol2_files.append(FileResponse(mol2_file_path, media_type="text/mol2"))
    return {
        "images_2d": images,
        "images_3d": mol2_files,
    }


@app.websocket("/ws/transcribe")
async def websocket_transcribe(websocket: WebSocket):
    await websocket.accept()
    audio_buffer = b""
    while True:
        data = await websocket.receive_bytes()
        audio_buffer += data
        # Optionally, process in chunks for partial transcription
        if len(audio_buffer) > 16000:  # After 1 second of audio
            response_text = get_text_from_whisper(audio_buffer)
            await websocket.send_text(response_text)
            # audio_buffer = b""  # Reset buffer or keep for continuous context


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
