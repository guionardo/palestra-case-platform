import logging
import queue
import ssl
import urllib.error
import urllib.request
import urllib.response
from typing import Tuple

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE


def do_http_request(request: urllib.request.Request, timeout: int) -> Tuple[int, str]:

    try:
        with urllib.request.urlopen(request,
                                    context=CTX,
                                    timeout=timeout) as response:
            code = response.code
            if 0 < response.code < 500:
                body = response.read(response.length)
            else:
                body = ''
        return code, body
    except urllib.error.HTTPError as exc:
        if exc.readable():
            response_body = exc.read().decode('utf-8', errors='ignore')
        else:
            response_body = exc.reason
        return exc.code, response_body
    except urllib.error.URLError as exc:
        logging.error('URL Error #%s %s (%s)', exc.errno,
                      exc.strerror, exc.filename)
        raise
    except NotImplementedError:
        raise
    except Exception as exc:
        logging.error('Response error %s', exc)
        raise


def get_request(method: str, url: str, filename: str) -> urllib.request.Request:
    with open(filename, 'b') as file:
        data = file.read()
    if method.upper() in ['POST', 'PUT']:
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Content-Length': len(data)
        }

        request = urllib.request.Request(
            url, data, headers, method=method)

    elif method.upper() == 'GET':
        request = urllib.request.Request(url, data, method='GET')

    else:
        raise NotImplementedError()

    return request


def send_file(filename: str,
              receiver_url: str,
              result_queue: queue.Queue,
              circuit_breaker: CircuitBreaker):
    circuit_breaker.wait(receiver_url)
    request = get_request('POST', receiver_url, filename)
    status_code, response_body = do_http_request(request, 30)
    if status_code >= 500:
        circuit_breaker.open(receiver_url)
    else:
        circuit_breaker.close(receiver_url)

    # Publica na fila de resultados, o retorno da operação
    result_queue.put((filename, status_code, response_body))


def get_receiver_url(filename: str) -> str:
    """
    Identifica a URL do serviço de recebimento a partir do nome do arquivo
    Código mockado neste exemplo, pois usamos regras específicas em produção.
    """
    return "https://api.localhost:8080"
