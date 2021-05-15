import snowflake.connector
from snowflake.connector import DictCursor
import snowflakecfg as cfg
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse, HTMLResponse

conn = snowflake.connector.connect(
    user=cfg.snowflake["username"],
    password=cfg.snowflake["password"],
    account=cfg.snowflake["region"],
    warehouse=cfg.snowflake["warehouse"],
    database=cfg.snowflake["database"],
    schema=cfg.snowflake["schema"]
)

# Defining the access key
API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"
COOKIE_DOMAIN = "localtest.me"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_cookie = APIKeyCookie(name=API_KEY_NAME, auto_error=False)


async def get_api_key(
        api_key_query: str = Security(api_key_query),
        api_key_header: str = Security(api_key_header),
        api_key_cookie: str = Security(api_key_cookie),
):
    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    elif api_key_cookie == API_KEY:
        return api_key_cookie
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")


# Initializing the FastApi
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/")
async def homepage():
    html_content = """
        <html>
            <head>
                <title>Assignment 3.1</title>
            </head>
            <body style="background-color:Black">
                <h1 style="background-color:#DAF7A6;text-align:center">API Access Key Authentication!</h1>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content)


# Clears the cookie
@app.get("/logout-streamlit")
async def route_logout_and_remove_cookie():
    content = {"message": "Logged Out Successfully!"}
    response = JSONResponse(content=content)
    response.delete_cookie(API_KEY_NAME, domain=COOKIE_DOMAIN)
    return response


@app.get("/logout")
async def route_logout_and_remove_cookie():
    html_content = """
        <html>
            <head>
                <title>Assignment 3.1</title>
            </head>
            <body style="background-color:Black">
                <h1 style="background-color:#DAF7A6;text-align:center">Logged Out Successfully!</h1>
                <h3 style="text-align:center;color:#DAF7A6">The cookie has been cleared!</h3>
            </body>
        </html>
        """
    response = HTMLResponse(content=html_content)
    response.delete_cookie(API_KEY_NAME, domain=COOKIE_DOMAIN)
    return response


# Opens the Swagger UI
@app.get("/openapi.json", tags=["documentation"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    response = JSONResponse(
        get_openapi(title="FastAPI security test", version=1, routes=app.routes)
    )
    return response


# Sets the swagger UI along with cookie
@app.get("/documentation", tags=["documentation"])
async def get_documentation(api_key: APIKey = Depends(get_api_key)):
    response = get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

    response.set_cookie(
        API_KEY_NAME,
        value=api_key,
        domain=COOKIE_DOMAIN,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response


# Sets the access key in cookie
@app.get("/login", tags=["login"])
async def get_login(api_key: APIKey = Depends(get_api_key)):
    html_content = """
            <html>
                <head>
                    <title>Assignment 3.1</title>
                </head>
                <body style="background-color:Black">
                    <h1 style="background-color:#DAF7A6;text-align:center">Access Granted!</h1>
                    <h3 style="text-align:center;color:#DAF7A6">Access key set in: COOKIE</h3>
                </body>
            </html>
            """
    response = HTMLResponse(content=html_content)

    response.set_cookie(
        API_KEY_NAME,
        value=api_key,
        domain=COOKIE_DOMAIN,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response

# Sets the access key in cookie
@app.get("/login-streamlit", tags=["login"])
async def get_login(api_key: APIKey = Depends(get_api_key)):
    content = {"message": "Logged In Successfully!"}
    response = JSONResponse(content=content)

    response.set_cookie(
        API_KEY_NAME,
        value=api_key,
        domain=COOKIE_DOMAIN,
        httponly=True,
        max_age=1800,
        expires=1800,
    )
    return response


# For testing endpoint acccess
@app.get("/login_data", tags=["test"])
async def get_login(api_key: APIKey = Depends(get_api_key)):
    html_content = """
            <html>
                <head>
                    <title>Assignment 3.1</title>
                </head>
                <body style="background-color:Black">
                    <h1 style="background-color:#DAF7A6;text-align:center">Access Granted!</h1>
                    <h3 style="text-align:center;color:#DAF7A6">Access key set in: Cookie | Header | Query Parameter</h3>
                </body>
            </html>
            """
    response = HTMLResponse(content=html_content)
    return response

# For testing endpoint acccess
@app.get("/secure_endpoint", tags=["test"])
async def get_open_api_endpoint(api_key: APIKey = Depends(get_api_key)):
    html_content = """
                <html>
                    <head>
                        <title>Assignment 3.1</title>
                    </head>
                    <body style="background-color:Black">
                        <h1 style="background-color:#DAF7A6;text-align:center">Access Granted!</h1>
                        <h3 style="text-align:center;color:#DAF7A6">Access key set in: Cookie | Header | Query Parameter</h3>
                    </body>
                </html>
                """
    response = HTMLResponse(content=html_content)
    return response


# Gets all the data from stagging snowflake database
@app.get("/all", tags=["all"])
async def get_all(api_key: APIKey = Depends(get_api_key)):
    cur = conn.cursor()

    data = cur.execute("""SELECT * FROM identifier('"LENDING_CLUB"."PUBLIC"."LENDING_CLUB_LOAN_TWO"') limit 1""")
    response = []
    for t in data:
        response.append(t)

    return {"data": response}


# Gets the data by specific verification status
@app.get("/verification_details/{VERIFICATION_STATUS}", tags=["Verification_Status"])
def verification_details(VERIFICATION_STATUS: str, api_key: APIKey = Depends(get_api_key)):

    cur = conn.cursor(DictCursor)
    list = ['Source Verified', 'Verified', 'Not Verified']
    if VERIFICATION_STATUS not in list:
        raise HTTPException(status_code=404, detail="Item not found")

    response = []
    cur.execute("""SELECT * FROM identifier('"LENDING_CLUB"."PUBLIC"."LENDING_CLUB_LOAN_TWO"') limit 50""")
    for rec in cur:
        if rec['VERIFICATION_STATUS'] == VERIFICATION_STATUS:
            response.append(rec)

    return {"data": response}


# Gets data by specified loan purpose
@app.get("/purpose/{PURPOSE}", tags=["Purpose"])
def purpose(PURPOSE: str):

    cur = conn.cursor(DictCursor)

    response = []
    cur.execute("""SELECT * FROM identifier('"LENDING_CLUB"."PUBLIC"."LENDING_CLUB_LOAN_TWO"') limit 50""")
    for rec in cur:
        if rec['PURPOSE'] == PURPOSE:
            response.append(rec)

    return {"data": response}


# Gets data by specified loan amount
@app.get("/loan_amount/{LOAN_AMNT}", tags=["Loan Amount"])
def loan_amount(LOAN_AMNT: int):

    cur = conn.cursor(DictCursor)

    response = []
    cur.execute("""SELECT * FROM identifier('"LENDING_CLUB"."PUBLIC"."LENDING_CLUB_LOAN_TWO"') limit 50""")
    for rec in cur:
        if rec['LOAN_AMNT'] == LOAN_AMNT:
            response.append(rec)

    return {"data": response}


# Gets the data by specified home ownership and annual income greater than specified
@app.get("/ownership_income/{HOME_OWNERSHIP},{ANNUAL_INC}", tags=["Home Ownership and Annual Income"])
def ownership_income(HOME_OWNERSHIP: str, ANNUAL_INC: int):
    cur = conn.cursor(DictCursor)
    try:
        response = []
        cur.execute("""SELECT * FROM identifier('"LENDING_CLUB"."PUBLIC"."LENDING_CLUB_LOAN_TWO"') limit 50""")
        for rec in cur:
            if (rec['HOME_OWNERSHIP'] == HOME_OWNERSHIP and rec['ANNUAL_INC'] > ANNUAL_INC):
                response.append(rec)

        return {"data": response}
    finally:
        cur.close()


# Gets the count of each verification status
@app.get("/GET_COUNT", tags=["GET_COUNT"])
def GET_COUNT_by_LOAN_STATUS(api_key: APIKey = Depends(get_api_key)):
    cur = conn.cursor(DictCursor)
    response = []
    cur.execute(
        """SELECT LOAN_STATUS,COUNT(*) as Count FROM identifier('"LENDING_CLUB"."PUBLIC"."LENDING_CLUB_LOAN_TWO"') GROUP BY LOAN_STATUS""")
    for rec in cur:
        response.append(rec)

    return {"data": response}
