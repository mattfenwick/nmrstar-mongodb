import nmrpystar.parse as np
import json
import glob
import re


re_number = re.compile("bmrb(\d+)\.txt")

def parseAll(paths, log):
    for path in paths:
        with open(path, 'r') as f:
            parsed = np.parse_nmrstar_ast(f.read())
            my_id = re_number.search(path).groups()[0]
            if parsed.status == 'success':
                log.append(dict(type='success', id=my_id))
                # TODO do something with the parse tree
            else:
                log.append(dict(type='failure', id=my_id, error=parsed.value)


def getFiles(path='data'):
    # see http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
    return glob.glob("%s/*" % path)

log = []
parseAll(getFiles(), log)
print json.dumps(log, indent=2)

