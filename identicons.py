from fastapi import FastAPI, Query, Response
from identiconsGenerator import identicons
from randomAvatarGenerator import randomAvatar

app = FastAPI(title="Identicons Generator")


@app.get("/identicon/", summary="Get unique identicon")
async def generate_identicon(string: str = Query(..., title="String to generate Identicon for"),
                             size: int = Query(100, title="Size of the Identicon")):

    return Response(content=identicons(string, size), media_type="image/png")

@app.get("/avatar/", summary="Get randomly generated identicon")
async def generate_identicon(size: int = Query(100, title="Size of the Avatar")):

    return Response(content=randomAvatar(size), media_type="image/png")



