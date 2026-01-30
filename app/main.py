from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
	return {"message": "Project 2 CI/CD Auto Deploy is Working!"}
@app.get("/health")
def health():
	return {"Status": "Healthy"}
