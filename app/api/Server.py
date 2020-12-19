import uvicorn

Configuration = uvicorn.config.Config


# Example configuration
#
# default_config = Configuration(
#     "api.test:app",
#     host="0.0.0.0",
#     port=8000,
#     debug=True,
#     log_config=None
# )


class Server(uvicorn.Server):
    pass
