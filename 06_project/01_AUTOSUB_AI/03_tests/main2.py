import requests

def main():
    with open('data.json', 'r') as f:
        data = json.load(f)
    print(data)
    print(data['name'])



def greet(greeting):
    """_summary_

    Args:
        greeting (_type_): _description_

    Returns:
        _type_: _description_
    """
    return f'{greeting} World!'