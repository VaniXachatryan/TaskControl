import uvicorn
from fastapi import FastAPI

from src.presentation.api.routes.routes import all_routers

app = FastAPI(
    title="Контроль заданий на выпуск продукции"
)

for router in all_routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
