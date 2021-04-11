from psutil import win_service_get


def check_win_service():
    """
    This function checks for the 'MYSQL80' service on a WINDOWS machine and returns it's status.
    :return: The status of the MYSQL80 service. It will be either 'stopped' or 'running'.
    """
    service_name = 'MYSQL80'
    try:
        service = win_service_get(service_name)
        service_status = service.status()
    except Exception as error:
        return f"An error occurred during the execution of the script.\nMore details: {error}"
    else:
        return service_status


if __name__ == '__main__':
    print(check_win_service())
