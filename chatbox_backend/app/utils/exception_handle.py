from fastapi import HTTPException, status

def exception_handler(e):

  if isinstance(e, HTTPException):
    return HTTPException(
      status_code=e.status_code,
      detail=e.detail
    )
  else:
    return HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail="HTTP_500_INTERNAL_SERVER_ERROR"
    )