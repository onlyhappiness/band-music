def is_hangul(text):
    """
    문자열이 한글로만 이루어져있는지 확인하는 함수
    """
    if not text:
        return False
    
    for char in text:
        if not (0xAC00 <= ord(char) <= 0xD7A3):
            return False
    return True

def _has_final_consonant(char):
    """
    받침이 있는지 확인하는 내부 함수
    """
    if not char or not isinstance(char, str):
        return False
    code = ord(char[-1]) - 0xAC00
    if code < 0 or code > 11172:
        return False
    return bool(code % 28)

def get_은는(name):
    return "은" if _has_final_consonant(name) else "는"

def get_이가(name):
    return "이" if _has_final_consonant(name) else "가"


def get_을를(name):
    return "을" if _has_final_consonant(name) else "를"

def get_으로(name):
    return '으로' if _has_final_consonant(name) else '로'
