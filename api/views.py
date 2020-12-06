import asyncio
from django.http import HttpResponse


async def index(request):
    await asyncio.sleep(15)
    return HttpResponse("Hello, async Django!")


async def mock_view(request):
    return HttpResponse("Second View!")
