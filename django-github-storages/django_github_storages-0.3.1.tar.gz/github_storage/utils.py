from django.conf import settings


def get_url(name, path, media_bucket):
    """
    Helper function to construct the url of the file.
    """
    url = "https://api.github.com/repos/"
    url += f"{str(settings.GITHUB_HANDLE)}/"
    url += str(settings.GITHUB_REPO_NAME)
    url += "/contents/"

    url += str(name) if media_bucket is None else f"{str(media_bucket)}/"
    if len(path) != 0:
        for folder_name in path:
            url += f"{str(folder_name)}/"

    url += str(name)

    return url
