
from src.routes.invoice import route as InvoiceRoute
from src.routes.auth import route as AuthRoute
from fastapi import FastAPI
app = FastAPI()

app.include_router(InvoiceRoute, prefix="/invoice", tags=["Invoice"])
app.include_router(AuthRoute, tags=["Auth"])
