# Backend server

## Installation steps

Create new virtual environment
```
python -m venv venv
```

Activate the environment

a) Linux:
```
source venv/bin/activate
```
b) Windows:
```
venv\Scripts\activate
```

Upgrade pip
```
python -m pip install --upgrade pip
```

Install all dependencies
```
pip install -r requirements.txt
```

Install this package as editable
```
pip install -e .
```

Verify the installation by running tests
```
pytest
```

## Running the server

Start the server
```
python -m server
```

The server should be now running on `http://127.0.0.1:3000`.

To see all available parameters for server startup customization run
```
python -m server -h
```

[Here](sample_requests_and_responses) are sample requests and responses for all of the endpoints.
Each subdirectory includes a response (and optionally a request) for a specific endpoint.