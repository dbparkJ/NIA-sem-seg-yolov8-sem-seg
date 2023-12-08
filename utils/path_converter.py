"""
주어진 경로에서 '\'를 '/'로 바꾸는 함수입니다.

Args:
    path (str): 경로 문자열

Returns:
    str: '\'를 '/'로 바꾼 경로 문자열
"""
class PathConverter:
    @staticmethod
    def convert_backslash_to_slash(path):
        return path.replace('\\', '/')