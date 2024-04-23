from fastapi import FastAPI, Query, Response, HTTPException
from identiconsGenerator import identicons
from randomAvatarGenerator import randomAvatar

app = FastAPI(title="Identicons Generator")


@app.get("/identicon/", summary="Get unique identicon")
async def generate_identicon(string: str = Query(..., title="String to generate Identicon for"),
                             size: int = Query(100, title="Size of the Identicon")):

    if size <= 1080:
        return Response(content=identicons(string, size), media_type="image/png")
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/avatar/", summary="Get randomly generated identicon")
async def generate_identicon(size: int = Query(100, title="Size of the Avatar")):

    if size <= 1080:
        return Response(content=randomAvatar(size), media_type="image/png")
    else:
        raise HTTPException(status_code=404, detail="Item not found")



