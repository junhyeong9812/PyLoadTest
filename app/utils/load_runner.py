import requests
from concurrent.futures import ThreadPoolExecutor
from app.schemas import LoadTestRequest


def send_request(session, method, url, **kwargs):
    try:
        response = session.request(method=method, url=url, **kwargs)
        return {"status": response.status_code}
    except Exception as e:
        return {"status": "error", "detail": str(e)}


def run_load_test(data: LoadTestRequest):
    results = []

    def task():
        with requests.Session() as session:
            result = send_request(
                session,
                data.method,
                data.url,
                params=data.params,
                headers=data.headers,
                data=data.body,
                cookies=data.cookies,
            )
            results.append(result)

    with ThreadPoolExecutor(max_workers=data.threads) as executor:
        for _ in range(data.total_requests):
            executor.submit(task)

    success = sum(1 for r in results if isinstance(r["status"], int) and r["status"] < 400)
    fail = data.total_requests - success
    return {"success": success, "fail": fail, "total": data.total_requests}
