import unittest, subprocess, psutil, os, time

class test_reg (unittest.TestCase):

    def test_renderImage(self):
        outputFileName = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/imageProperties/unitTestRender.txt"
        outputRenderName = "unitTestRender.jpg"
        subprocess.Popen(['python', 
        'C:/Users/danie/Documents/GitHub/CSC7058/PythonFiles/parseProperties.py', outputFileName, outputRenderName])
        imageFileName = "C:/Daz 3D/Applications/Data/DAZ 3D/Render Library/unitTestRender.jpg"
        imageFound = False
        test = 0
        #check if image exists and relocate to /static/RenderLibrary/
        while not (imageFound):
            if os.path.exists(imageFileName):
                time.sleep(2)
                for proc in psutil.process_iter():
                    try:
                        # Get process name & pid from process object.
                        processName = proc.name()
                        #killing process from task manager to ensure no conflict with relaunching Daz Studio
                        procname = "DAZStudio.exe"
                        if processName == procname:
                            proc.kill()
                    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass

                renderedImage = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/RenderLibrary/" + outputRenderName + ".jpg"
                os.rename(imageFileName, renderedImage)
                renderedImageMoved = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/RenderLibrary/" + outputRenderName + ".jpg"

                if os.path.exists(renderedImageMoved):
                    test = 1
                imageFound = True
        self.assertEqual(test, 1, "Should be 1")

if __name__ == "__main__":
    unittest.main()