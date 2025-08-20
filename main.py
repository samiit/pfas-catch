"""Main file rendering the APIs"""

from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles


from src.utils import (
    get_best_adsorber_pfas_table,
    get_filename,
    get_molecules,
    get_smiles,
)

app = FastAPI()

html_path = Path("templates") / "app.html"
html_content = html_path.read_text(encoding="utf-8")
# Mount static files (for serving images and mol2 files)
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/")
def get_pfas_match_root():
    """Base API for PFAS to Adsorber match"""
    return {"PFAS": "DETA-adsorber"}


@app.get("/app", response_class=HTMLResponse)
async def render_pfas_analysis_page():
    """Render the main PFAS analysis page"""
    return HTMLResponse(content=html_content, status_code=200)


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
async def get_images_from_text(request: Request):
    """Returns a list of image files from the text description of the molecule"""
    # Get form data
    form_data = await request.form()
    query = form_data.get("query", "")
    if not query:
        return {"error": "No query provided"}
    molecule_names = get_molecules(query)
    images = []
    mol2_files = []
    images_adsorbers = []
    mol2_files_adsorbers = []
    pfas_table_dict = {}
    for molecule_name in molecule_names:
        smiles = get_smiles(molecule_name)
        filename = get_filename(smiles) + ".jpg"
        file_path = Path("images") / filename
        images.append(FileResponse(file_path, media_type="image/jpg"))

        mol2_filename = get_filename(smiles) + "_gaff.mol2"
        mol2_file_path = Path("images") / mol2_filename
        mol2_files.append(FileResponse(mol2_file_path, media_type="text/mol2"))
        if "per-fluoro" in molecule_name:
            # if the molecule is a PFAS
            # Fetch the binding table for the PFAS
            pfas_table_dict = get_best_adsorber_pfas_table(molecule_name)
            adsorber_name = "DETA_" + pfas_table_dict[0].get("DETA_variant")
            image_adsorber = adsorber_name + ".jpg"
            image_adsorber_path = Path("images") / image_adsorber
            images_adsorbers.append(
                FileResponse(image_adsorber_path, media_type="image/jpg")
            )
            mol2_adsorber = adsorber_name + "_gaff.mol2"
            mol2_adsorber_path = Path("images") / mol2_adsorber
            mol2_files_adsorbers.append(
                FileResponse(mol2_adsorber_path, media_type="text/mol2")
            )

    # output_text = f"Generated images for: {', '.join(molecule_names)}"
    # _ = await text_to_speech(output_text)
    return {
        "images_2d": images,
        "images_3d": mol2_files,
        "best_adsorber": adsorber_name,
        "images_adsorbers": images_adsorbers,
        "mol2_files_adsorbers": mol2_files_adsorbers,
        "pfas_table": pfas_table_dict,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
