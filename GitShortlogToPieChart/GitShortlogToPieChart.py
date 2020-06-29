import matplotlib.pyplot as plt

#-------------------------

def generateExampleChart():
        # modified example taken from: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html
        # and: https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs' # list
        sizes = [15, 30, 45, 10] # array
        #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,
                #explode=explode,
                labels=labels,
                autopct='%1.1f%%',
                shadow=False,
                startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()

#-------------------------

def prepareFileContent():
        results = dict()
        with open('testdata.csv') as file:
                for line in file.readlines():
                        # trim it from whitespace
                        strippedLine = line.strip()
                        #print(strippedLine)  # todom remove
                        # split at first occasion of " "
                        amount, name = strippedLine.split(' ', 1)
                        #print(name, amount)  # todom remove
                        # just take the name, not the mail - else the legend is too long
                        key = list(name.split('<'))[0].rstrip()
                        results[key] = amount

        return results

#-------------------------

def renderPieChart(fileContentDict):
        print(fileContentDict) # todom  remove

        # data preparation
        labels = fileContentDict.keys()
        sizes = fileContentDict.values()

        # chart creation
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,
                #explode=explode,
                labels=labels,
                autopct='%1.1f%%',
                shadow=False,
                startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()
        #plt.savefig('GitShortlogToPieChart.png') # todo make this configureable by the user

        return plt

#-------------------------

def invokeGit():
        # call "git shortlog -sne --no-merges" and get the output; check for this at the upload-script
        import subprocess
        git = subprocess.Popen(
                #["mspaint.exe"], # does at least this work? yes :/
                ["git", "shortlog", "HEAD", "-sne"], # hint: the commit to checkout was missing, so it failed, it was not the minus!
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True
        )
        stdout, stderr = git.communicate()
        # check the return code for errors
        if git.returncode != 0:
                raise Exception(f"Something failed while invoking the git-command. Returncode: {git.returncode}")
                # Exception: Something failed while invoking the git-command. Returncode: 1; same happens with subprocess.run .. I guess the problem is that the git cmd is not resolved?!?

        # just for checking
        stdOut = stdout.decode('ascii')
        print("stdout:\n", stdOut, "\nlen:", stdOut.__len__())
        print("stderr:\n", stderr.decode('ascii'))

        textToUse = (" ".join(str(x)) for x in stdOut)
        print("textToUse:", textToUse)

        # split the stringified output and process it have a proper input for the chart renderer
        results = dict()
        for line in textToUse:
                print("line:", line) # todom remove
                continue
                strippedLine = line.strip()
                print("strippedLine:", strippedLine) # todom remove
                # avoid processing empty lines
                if not strippedLine:
                        continue
                # split at first occasion of " "
                amount, name = strippedLine.split(' ', 1)
                #print(name, amount)  # todom remove
                # just take the name, not the mail - else the legend is too long
                key = list(name.split('<'))[0].rstrip()
                results[key] = amount

        return results
        
#-------------------------

### from csv file ###
#fileContentDict = prepareFileContent()
#plot = renderPieChart(fileContentDict)
#plot.savefig('GitShortlogToPieChart.png', bbox_inches='tight')

#-------------------------

### from git ###
content = invokeGit()
content = renderPieChart(content)
#plot.savefig('GitShortlogToPieChart.png', bbox_inches='tight')

#-------------------------
