from fastapi import APIRouter, Depends, UploadFile, File, BackgroundTasks
from src.core.security import require_admin

router = APIRouter(prefix="/admin/products", tags=["admin"])

@router.post("/import")
async def import_products(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    admin=Depends(require_admin),
):
    """Upload CSV; validate and import products in the background."""
    background_tasks.add_task(process_csv_import, file)
    return {"job_id": "..."}

@router.get("/import/{job_id}")
async def import_status(job_id: str, admin=Depends(require_admin)):
    """Check status and error log for an import job."""
    pass
