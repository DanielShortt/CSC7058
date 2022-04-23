import unittest, winreg, json, subprocess, psutil, os, time

class test_reg (unittest.TestCase):
        
        
        def test_renderProps1(self):
                imageproperties = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/imageProperties/unitTestRender.txt"

                #Open the image properties file.
                with open(imageproperties) as file1:
                    imageproperties = json.load(file1)

                environmentKeys = imageproperties['Environment'][0]    

                for i in environmentKeys:
                    if (environmentKeys[i] == "Beach" ):
                        test1 = 1
                self.assertEqual(test1, 1, "Should be 1")


        def test_renderProps2(self):

            imageproperties = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/imageProperties/unitTestRender.txt"

            #Open the image properties file.
            with open(imageproperties) as file1:
                imageproperties = json.load(file1)

            environmentKeys = imageproperties['Environment'][0]    

            environmentKeys["Time"] = "Night"

            for i in environmentKeys:
                if (environmentKeys["Time"] == "Night" ):
                    #print("Found")
                    test2 = 1
            self.assertEqual(test2, 1, "Should be 1")
            

if __name__ == "__main__":
    unittest.main()