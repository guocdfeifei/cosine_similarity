def handle_upload_file(file):
    ftext = ''
    with open('name.txt', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            ftext = ftext + chunk.decode('utf-8')
    return ftext