#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

""" Common set of managament methods to be used by
 the different management api classes """

import os

# nuvla_endpoint_raw = os.environ["NUVLA_ENDPOINT"] if "NUVLA_ENDPOINT" in os.environ else "nuvla.io"
# while nuvla_endpoint_raw[-1] == "/":
#     nuvla_endpoint_raw = nuvla_endpoint_raw[:-1]
#
# nuvla_endpoint_insecure_raw = os.environ["NUVLA_ENDPOINT_INSECURE"] if "NUVLA_ENDPOINT_INSECURE" in os.environ else False
# if isinstance(nuvla_endpoint_insecure_raw, str):
#     if nuvla_endpoint_insecure_raw.lower() == "false":
#         nuvla_endpoint_insecure_raw = False
#     else:
#         nuvla_endpoint_insecure_raw = True
# else:
#     nuvla_endpoint_insecure_raw = bool(nuvla_endpoint_insecure_raw)
#
# nuvla_endpoint_insecure = nuvla_endpoint_insecure_raw
#
# nuvla_endpoint = nuvla_endpoint_raw.replace("https://", "")

data_volume = "/srv/nuvlabox/shared"
log_filename = "management-api.log"

activation_flag = "{}/.activated".format(data_volume)
nuvla_configuration = f'{data_volume}/.nuvla-configuration'

server_cert_file = "server-cert.pem"
server_key_file = "server-key.pem"
client_cert_file = "cert.pem"
client_key_file = "key.pem"
ca_file = "ca.pem"

nuvlabox_api_certs_folder = data_volume

provided_pubkey = os.getenv("NUVLABOX_SSH_PUB_KEY")
host_ssh_folder = "/hostfs/.ssh"

host_home_user = os.getenv("HOST_USER", os.getenv('HOME'))
ssh_user = host_home_user if host_home_user else "root"

return_404 = {"status": 404,
              "message": "undefined"}

return_405 = {"status": 405,
              "message": "undefined"}

return_200 = {"status": 200,
              "message": "undefined"}

return_201 = {"status": 201,
              "message": "undefined"}

return_400 = {"status": 400,
              "message": "undefined"}

return_500 = {"status": 500,
              "message": "undefined"}

return_generic = {"status": "placeholder",
                  "message": "undefined"}

