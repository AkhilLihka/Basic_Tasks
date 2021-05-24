from zipfile import ZipFile
import os
import shutil
import json

src = "C:/tenant/CDK Extracts/CDK Scripts/Extraction_agent/cdk_validation"
base = 'C:/tenant/CDK Extracts/CDK Scripts/Extraction_agent/'


def collect_file(filename):
    file = os.path.join(src, filename)
    with ZipFile(file, 'r') as zip:
        zip.extractall()
        if filename == 'ms_image.zip':
            dirfile = 'Macro Scheduler'
        else:
            dirfile = zip.namelist()[0].split('/')[0]

    if is_dir_exists(os.path.join("C:/", dirfile)):
        del_folder(os.path.join("C:/", dirfile))

    if filename == 'ms_image.zip':
        srcpath = os.path.join(base, 'ms_image', 'macro_schedular')
    else:
        srcpath = os.path.join(base, dirfile)

    print("file copying for folder --", srcpath)
    shutil.copytree(srcpath, os.path.join("C:/", dirfile))

    if filename == 'ms_image.zip':
        del_folder(os.path.join(base, 'ms_image'))
    else:
        del_folder(os.path.join(base, dirfile))
    del_folder(os.path.join(base, '__MACOSX'))


def validation_files():
    files = os.listdir('C:/tenant/CDK Extracts/CDK Scripts/Extraction_agent/cdk_validation')
    for file in files:
        if file == 'Macro Scheduler 15.zip' or file == 'ms_image.zip':
            collect_file(file)


def del_folder(path):
    shutil.rmtree(path)


def is_dir_exists(dir):
    if os.path.exists(dir):
        return True
    else:
        return False





from_path = "C:\\tenant\\tenant.txt"
def Update_Creds(File_name):
    with open(from_path, 'r') as Source_file:
        data = Source_file.readlines()
        data = data[len(data) - 2:]
        cred_ = ' '.join(data).replace('\n', '').replace('{', '').replace('}', '').split()
        if len(cred_) == 2:
            with open(r'C:\\tenant\\CDK Extracts\\CDK Scripts\\Extraction_agent\\config\\' + str(File_name), 'r+',encoding='utf-8') as Json_file:
                Json_data = json.load(Json_file)
                Json_data['username'] = cred_[0]
                Json_data['password'] = cred_[1]
                IP=Update_weburl()
                Json_data['web'] = f"http://{IP[0]}/bin/start/wsStart.application"
                Json_file.seek(0)
                json.dump(Json_data, Json_file, ensure_ascii=False, indent=4)
                Json_file.truncate()
                print('Credentails Updated in', File)
        else:
            print("Credential  not found in Tenant file", cred_)


def Update_weburl():
    Host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"

    with open(Host_path, 'r') as Host_File:
        data = Host_File.readlines()
        data = data[len(data) - 1:]
        cred_ = ' '.join(data).replace('\n', '').replace('{', '').replace('}', '').split()
        return cred_[:1]

for File in ['validation_configAp.json', 'validation_config.json']:
    Update_Creds(File)


validation_files()

