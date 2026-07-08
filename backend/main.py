"""
Main entry point for the UAP-OS Backend application.
"""
import os
from typing import Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Application configuration
APP_NAME = os.getenv("APP_NAME", "UAP-OS Backend")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# CORS configuration
CORS_ORIGINS = os.getenv("CORS_ORIGINS", '["http://localhost:3000"]')
CORS_ALLOW_CREDENTIALS = os.getenv("CORS_ALLOW_CREDENTIALS", "True").lower() == "true"
CORS_ALLOW_METHODS = os.getenv("CORS_ALLOW_METHODS", '["*"]')
CORS_ALLOW_HEADERS = os.getenv("CORS_ALLOW_HEADERS", '["*"]')


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application lifespan events.
    """
    # Startup event
    print(f"🚀 Starting {APP_NAME} v{APP_VERSION}")
    print(f"📝 Environment: {ENVIRONMENT}")
    yield
    # Shutdown event
    print(f"🛑 Shutting down {APP_NAME}")


# Create FastAPI application
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Backend API for UAP-OS project",
    debug=DEBUG,
    lifespan=lifespan,
)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS.replace("'", '"'),
    allow_credentials=CORS_ALLOW_CREDENTIALS,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/", tags=["Health"])
async def root() -> dict:
    """Root endpoint - Health check"""
    return {
        "message": "UAP-OS Backend is running",
        "app": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
    }


@app.get("/health", tags=["Health"])
async def health() -> dict:
    """Health check endpoint"""
    return {
        "status": "ok",
        "app": APP_NAME,
        "version": APP_VERSION,
    }


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=DEBUG,
        log_level="info",
    )
