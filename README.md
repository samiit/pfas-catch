# PFAS-Catch 🧪🎙️

**TechEurope Hackathon Berlin 2025 - Voice Agent Track**
*"Agents That Act" - Voice-Controlled AI for Molecular Discovery*

An intelligent voice-controlled agent that transforms natural language descriptions into molecular discovery and visualization through AI-powered semantic search, chemical informatics, and autonomous task execution.

Here is the video demonstration of the submission: [Download Demo Video](https://drive.google.com/file/d/1q7I1suQlWol1CHcKXmZfSbBtwTPGl6Eh/view?usp=drive_link)


## 🎯 Project Vision

PFAS-Catch revolutionizes molecular discovery by enabling voice-driven conversations about chemical compounds. Simply speak your requirements, and our autonomous agent will search, identify, analyze, and visualize candidate molecules that match your needs - completing the entire workflow from voice input to molecular visualization.

## 🎙️ Voice Agent Architecture

```
Voice Input → AI-Coustics Enhancement → Telli Agent → Weaviate Search → SMILES → Visualization
```

### 1. **Voice Interface & Enhancement**
- **Telli.com Voice Agents** - Natural conversation with chemical domain expertise
- **AI-Coustics Audio Enhancement** - Studio-quality audio processing for clear speech recognition
- Context-aware dialogue management for complex molecular requirements
- Multi-turn conversations with clarification capabilities

### 2. **Autonomous Agent Execution**
- **Specialist Chemical Agents** - Domain experts in molecular science and PFAS chemistry
- **Task Planning & Execution** - Multi-step workflow automation
- **Error Handling & Recovery** - Intelligent error management and user feedback
- **Integration Orchestration** - Seamless API coordination across services

### 3. **Semantic Vector Search**
- **Weaviate Vector Database** - Metadata-enhanced chemical compound storage
- **Hybrid Search** - Combining vector similarity with keyword matching
- **Real-time Indexing** - Dynamic molecular database updates
- **Property-Based Filtering** - Solubility, toxicity, biodegradability criteria

### 4. **Molecular Output & Visualization**
- **SMILES Generation** - Standardized chemical structure representation
- **3D Molecular Rendering** - Interactive structure visualization
- **Property Analysis** - Automated chemical property prediction
- **Comparative Results** - Side-by-side candidate evaluation

## 🎯 Voice Agent Challenge Compliance

### **Task Execution Requirements** ✅
- **Voice Interface**: Natural language understanding with Telli voice agents
- **End-to-End Workflows**: Complete molecular discovery pipeline automation
- **Multi-API Integration**: Telli + AI-Coustics + Weaviate + Visualization APIs
- **Autonomous Decision Making**: Error handling, clarification requests, result prioritization

### **Example Voice Interaction**

**User**: *"I need help finding molecules that can break down PFAS compounds in water. They should be biodegradable, non-toxic to marine life, and effective at low concentrations."*

**Agent Workflow**:
1. **Audio Enhancement** - AI-Coustics processes speech for clarity
2. **Intent Recognition** - Telli agent understands molecular requirements
3. **Database Search** - Weaviate performs semantic search across chemical databases
4. **Property Filtering** - Applies biodegradability and toxicity constraints
5. **Result Analysis** - Evaluates effectiveness and concentration requirements
6. **Visualization** - Generates 3D models and property comparisons
7. **Voice Response** - Explains findings and asks for refinements

## 🚀 Technology Stack

### **Core Voice & AI**
- **Telli.com** - Voice agent framework with natural conversation capabilities
- **AI-Coustics** - Real-time audio enhancement and noise reduction
- **Python 3.12+** - Modern language features and async processing

### **Data & Search**
- **Weaviate** - Vector database for semantic molecular search
- **SMILES Processing** - Chemical structure parsing and validation
- **Molecular Databases** - PubChem, ChEMBL integration capabilities

### **Visualization & Output**
- **3D Molecular Rendering** - Interactive chemical structure display
- **Property Prediction** - ML-based chemical property modeling
- **Export Formats** - Multiple output formats for further analysis

## 📁 Project Structure

```
pfas-catch/
├── src/
│   ├── voice/              # Telli agent configuration and handlers
│   ├── audio/              # AI-Coustics integration and processing
│   ├── agents/             # Autonomous task execution logic
│   ├── database/           # Weaviate vector database integration
│   ├── chemistry/          # SMILES processing and molecular validation
│   ├── visualization/      # 3D rendering and property display
│   └── orchestration/      # Multi-API workflow coordination
├── tests/                  # Comprehensive test suite
├── data/                   # Chemical databases and vector embeddings
├── config/                 # API keys and service configurations
├── pyproject.toml          # Python dependencies and build config
└── README.md
```

## 🛠️ Technology Setup & Getting Started

### **1. Weaviate Vector Database Setup**

#### Cloud Setup (Recommended)
```bash
# 1. Sign up at https://console.weaviate.cloud/
# 2. Create a new cluster
# 3. Note your cluster URL and API key

# Install Weaviate Python client
uv add weaviate-client

# Basic connection test
python -c "
import weaviate
client = weaviate.connect_to_wcs(
    cluster_url='YOUR_WCS_URL',
    auth_credentials=weaviate.auth.AuthApiKey('YOUR_API_KEY')
)
print('Connected to Weaviate!')
client.close()
"
```

#### Local Development Setup
```bash
# Using Docker Compose
curl -o docker-compose.yml https://configuration.weaviate.io/v2/docker-compose/docker-compose.yml

# Start Weaviate locally
docker-compose up -d

# Test local connection
python -c "
import weaviate
client = weaviate.connect_to_local()
print('Connected to local Weaviate!')
client.close()
"
```

### **2. AI-Coustics Audio Enhancement Setup**

#### SDK Integration
```bash
# Contact AI-Coustics for SDK access
# Visit: https://ai-coustics.com/sdk/

# Install their SDK (example structure)
# uv add ai-coustics-sdk

# API Integration (if using their API)
curl -X POST "https://api.ai-coustics.com/v1/enhance" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @input_audio.wav
```

#### Real-time Enhancement Setup
```python
# Example integration pattern
from ai_coustics import AudioEnhancer

enhancer = AudioEnhancer(api_key="YOUR_API_KEY")

# Real-time audio processing
def enhance_audio_stream(audio_data):
    return enhancer.enhance_realtime(audio_data)
```

### **3. Telli Voice Agent Setup**

#### Account & API Setup
```bash
# 1. Sign up at https://telli.com/
# 2. Access developer documentation
# 3. Obtain API credentials

# Install Telli SDK (hypothetical)
# uv add telli-sdk
```

#### Voice Agent Configuration
```python
# Example Telli integration
from telli import VoiceAgent, AgentConfig

config = AgentConfig(
    api_key="YOUR_TELLI_API_KEY",
    voice_model="conversational",
    domain="chemistry",
    language="en-US"
)

agent = VoiceAgent(config=config)

# Define chemical domain knowledge
agent.add_domain_knowledge({
    "molecular_properties": ["solubility", "toxicity", "biodegradability"],
    "chemical_databases": ["pubchem", "chembl"],
    "output_formats": ["smiles", "sdf", "mol"]
})
```

### **4. Python Environment Setup**

```bash
# Install uv package manager
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create project
uv init pfas-catch
cd pfas-catch

# Add core dependencies
uv add weaviate-client pydantic fastapi rdkit-pypi requests aiohttp

# Add development dependencies
uv add --dev pytest black mypy ruff
```

## 🔗 Step-by-Step Integration Guide

### **Phase 1: Foundation Setup**

#### Step 1: Environment Configuration
```bash
# 1. Clone repository
git clone <repository-url>
cd pfas-catch

# 2. Setup Python environment
uv sync

# 3. Create configuration file
cp config/env.example .env
```

#### Step 2: Configure Environment Variables
```bash
# .env file configuration
WEAVIATE_URL=https://your-cluster.weaviate.network
WEAVIATE_API_KEY=your_weaviate_api_key
AI_COUSTICS_API_KEY=your_ai_coustics_key
TELLI_API_KEY=your_telli_api_key
OPENAI_API_KEY=your_openai_key  # For embeddings if needed
```

### **Phase 2: Vector Database Initialization**

#### Step 3: Setup Weaviate Schema
```python
# src/database/setup.py
import weaviate
from weaviate.classes.config import Configure, Property, DataType

def initialize_molecular_database():
    client = weaviate.connect_to_wcs(
        cluster_url=os.getenv("WEAVIATE_URL"),
        auth_credentials=weaviate.auth.AuthApiKey(os.getenv("WEAVIATE_API_KEY"))
    )

    # Create Molecule collection
    client.collections.create(
        name="Molecule",
        vectorizer_config=Configure.Vectorizer.text2vec_openai(),
        properties=[
            Property(name="smiles", data_type=DataType.TEXT),
            Property(name="name", data_type=DataType.TEXT),
            Property(name="molecular_weight", data_type=DataType.NUMBER),
            Property(name="solubility", data_type=DataType.TEXT),
            Property(name="toxicity_level", data_type=DataType.TEXT),
            Property(name="biodegradable", data_type=DataType.BOOL),
            Property(name="description", data_type=DataType.TEXT),
            Property(name="properties", data_type=DataType.TEXT_ARRAY)
        ]
    )
```

#### Step 4: Import Chemical Data
```python
# src/database/import_data.py
def import_pfas_molecules():
    molecules = client.collections.get("Molecule")

    sample_data = [
        {
            "smiles": "CC(C)(C)C(=O)O",
            "name": "Pivaloic acid",
            "molecular_weight": 102.13,
            "solubility": "high",
            "toxicity_level": "low",
            "biodegradable": True,
            "description": "Potential PFAS degradation catalyst",
            "properties": ["catalyst", "biodegradable", "water_soluble"]
        }
        # Add more molecules...
    ]

    with molecules.batch.dynamic() as batch:
        for molecule in sample_data:
            batch.add_object(properties=molecule)
```

### **Phase 3: Audio Processing Pipeline**

#### Step 5: AI-Coustics Integration
```python
# src/audio/enhancement.py
class AudioEnhancer:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.ai-coustics.com/v1"

    async def enhance_audio(self, audio_data: bytes) -> bytes:
        """Enhance audio quality using AI-Coustics API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "audio/wav"
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/enhance",
                headers=headers,
                data=audio_data
            ) as response:
                return await response.read()
```

### **Phase 4: Voice Agent Implementation**

#### Step 6: Telli Agent Integration
```python
# src/voice/telli_agent.py
class ChemicalVoiceAgent:
    def __init__(self, config: dict):
        self.telli_client = TelliClient(config["api_key"])
        self.audio_enhancer = AudioEnhancer(config["ai_coustics_key"])
        self.weaviate_client = weaviate.connect_to_wcs(
            cluster_url=config["weaviate_url"],
            auth_credentials=weaviate.auth.AuthApiKey(config["weaviate_key"])
        )

    async def process_voice_request(self, audio_input: bytes) -> dict:
        # 1. Enhance audio quality
        enhanced_audio = await self.audio_enhancer.enhance_audio(audio_input)

        # 2. Convert speech to text with chemical domain
        transcript = await self.telli_client.speech_to_text(
            enhanced_audio,
            domain="chemistry"
        )

        # 3. Extract molecular requirements
        requirements = await self.extract_molecular_requirements(transcript)

        # 4. Search vector database
        molecules = await self.search_molecules(requirements)

        # 5. Generate response
        response = await self.generate_voice_response(molecules)

        return {
            "transcript": transcript,
            "requirements": requirements,
            "molecules": molecules,
            "response_audio": response
        }
```

### **Phase 5: Molecular Search & Processing**

#### Step 7: Vector Search Implementation
```python
# src/agents/molecular_search.py
class MolecularSearchAgent:
    def __init__(self, weaviate_client):
        self.client = weaviate_client
        self.molecules = self.client.collections.get("Molecule")

    async def search_by_requirements(self, requirements: dict) -> list:
        # Hybrid search combining vector and filter
        response = self.molecules.query.hybrid(
            query=requirements["description"],
            where=self.build_filters(requirements),
            limit=10
        )

        return [obj.properties for obj in response.objects]

    def build_filters(self, requirements: dict):
        filters = []

        if requirements.get("biodegradable"):
            filters.append({"path": "biodegradable", "operator": "Equal", "valueBoolean": True})

        if requirements.get("max_toxicity"):
            filters.append({"path": "toxicity_level", "operator": "Equal", "valueText": "low"})

        return {"operator": "And", "operands": filters} if filters else None
```

### **Phase 6: Complete Workflow Orchestration**

#### Step 8: Main Application Integration
```python
# main.py
async def main():
    # Initialize all components
    config = load_config()

    voice_agent = ChemicalVoiceAgent(config)
    molecular_agent = MolecularSearchAgent(voice_agent.weaviate_client)
    visualizer = MolecularVisualizer()

    # Start voice interface
    print("🎙️ PFAS-Catch Voice Agent Ready!")
    print("Say: 'Find molecules that can break down PFAS compounds'")

    while True:
        # Capture audio input
        audio_input = await capture_microphone_input()

        # Process through complete pipeline
        result = await voice_agent.process_voice_request(audio_input)

        # Visualize results
        if result["molecules"]:
            visualizer.display_molecules(result["molecules"])

        # Play response
        await play_audio_response(result["response_audio"])

if __name__ == "__main__":
    asyncio.run(main())
```

### **Phase 7: Testing & Validation**

#### Step 9: Integration Testing
```python
# tests/test_integration.py
async def test_complete_pipeline():
    # Test audio enhancement
    enhanced = await audio_enhancer.enhance_audio(sample_audio)
    assert len(enhanced) > 0

    # Test voice agent
    result = await voice_agent.process_voice_request(sample_audio)
    assert result["transcript"]
    assert result["molecules"]

    # Test molecular search
    molecules = await molecular_agent.search_by_requirements({
        "description": "biodegradable PFAS breakdown",
        "biodegradable": True
    })
    assert len(molecules) > 0
```

#### Step 10: End-to-End Deployment
```bash
# Production deployment
docker build -t pfas-catch .
docker run -p 8000:8000 \
  -e WEAVIATE_URL=$WEAVIATE_URL \
  -e WEAVIATE_API_KEY=$WEAVIATE_API_KEY \
  -e AI_COUSTICS_API_KEY=$AI_COUSTICS_API_KEY \
  -e TELLI_API_KEY=$TELLI_API_KEY \
  pfas-catch
```

## 🏆 Hackathon Goals

### **MVP Objectives** (Voice Agent Track)
- [x] Define voice-controlled agent architecture
- [ ] Integrate Telli voice agent with chemical domain knowledge
- [ ] Implement AI-Coustics audio enhancement pipeline
- [ ] Set up Weaviate vector database with molecular embeddings
- [ ] Create autonomous workflow orchestration
- [ ] Build SMILES output and molecular validation
- [ ] Develop interactive 3D visualization interface

### **Advanced Features**
- [ ] Multi-turn conversational refinement
- [ ] Real-time molecular property prediction
- [ ] Integration with external chemical databases
- [ ] Voice-controlled parameter adjustment
- [ ] Export to computational chemistry formats

## 🧪 Use Cases & Applications

### **Environmental Applications**
1. **PFAS Remediation** - Finding biodegradable molecules for forever chemical breakdown
2. **Water Treatment** - Identifying safe, effective water purification compounds
3. **Pollution Control** - Discovering molecules for environmental cleanup

### **Voice Agent Advantages**
- **Accessibility** - Hands-free operation in laboratory environments
- **Speed** - Rapid iteration through spoken refinements
- **Natural Interaction** - Complex queries expressed in natural language
- **Multi-tasking** - Voice operation while performing other lab work

## 🔬 Scientific Foundation

### **Chemical Intelligence**
- Vector embeddings of molecular properties and structures
- Quantum chemistry databases for property prediction
- Expert knowledge graphs for molecular relationships
- Real-time toxicity and environmental impact assessment

### **Voice Agent Intelligence**
- Domain-specific training on chemical terminology
- Context preservation across multi-turn conversations
- Error detection and clarification strategies
- Autonomous task decomposition and execution

## 🎙️ Quick Start

```bash
# Complete setup in one go
git clone <repository-url>
cd pfas-catch
uv sync
cp config/env.example .env
# Add your API keys to .env
uv run python -m src.database.setup
uv run python main.py
```

## 🤝 Contributing

Built for TechEurope Hackathon Berlin 2025 - Voice Agent Track. We welcome contributions and collaboration from the scientific and AI communities!

## 📄 License

MIT License - TechEurope Hackathon Berlin 2025

---

*"Where voice meets molecular discovery - autonomous agents for scientific breakthrough"*
