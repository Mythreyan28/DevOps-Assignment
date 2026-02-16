from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# FIXED CORS CONFIGURATION - Allow frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://da-prod-alb-1813349231.us-east-1.elb.amazonaws.com",  # Your frontend URL
        "http://localhost:3000",  # Local development
        "http://localhost:8000",  # Local backend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def api_root():
    return {
        "message": "DevOps Assignment API",
        "status": "running",
        "endpoints": ["/health", "/message"]
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "message": "Backend is running successfully"}

@app.get("/api/message")
async def get_message():
    return {"message": "Hello from DevOps Assignment backend!"}
