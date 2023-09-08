from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import JSONResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
def get_time_and_day():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), datetime.utcnow().strftime("%A")
    
@app.get("/api")
def get_endpoint(slack_name, track):
    timer, day = get_time_and_day()
    return JSONResponse(content={
        "slack_name": slack_name,
        "current_day": day,
        "utc_time": timer,
        "track": track,
        "github_file_url": "https://github.com/TeflonX/HNGX/blob/master/main.py",
        "github_repo_url": "https://github.com/TeflonX/HNGX/tree/master",
        "status_code": 200
}, status_code=200)

if __name__ == '__main__':
    uvicorn.run(app="main:app", port=8000, reload=True )