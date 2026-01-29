from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
	return {
	    "Project1": "Project2",
            "message": "CI/CD pipeline: This is a test",
 	    "Status": "Running"
	       }
@app.get("/health")
def health():
	return {"Status": "Healthy"}
