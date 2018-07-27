import os

from KeyMatcher import MatchKeys


class FileScanner:
    def __init__(self, ):
        self.matcher = MatchKeys()

    def scan_filesystem(self, path, keys_to_match, files_found):
        count = 0
        try:
            for entry in os.scandir(path):
                if entry.is_dir(follow_symlinks=False):
                    count += self.scan_filesystem(entry.path, keys_to_match, files_found)
                else:
                    matched_key = self.matcher.match_key((entry.name, keys_to_match))
                    if matched_key is not None:
                        files_found.append((matched_key, entry.name, entry.path))
                    count += 1
        except PermissionError as err:
            print("Access Error error: {0}".format(err))
        except OSError as err:
            print("OS Error error: {0}".format(err))
        return count
