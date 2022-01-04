# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        self.vertices =  [self.parameters['position'],
          fusion(self.parameters['position'],[0,0,self.parameters['height']]),
          fusion(self.parameters['position'],[self.parameters['width'], 0, self.parameters['height']]),
          fusion(self.parameters['position'],[self.parameters['width'], 0, 0]),
          fusion(self.parameters['position'],[0,self.parameters['thickness'],0]),
          fusion(self.parameters['position'],[0,self.parameters['thickness'],self.parameters['height']]),
          fusion(self.parameters['position'],[self.parameters['width'],self.parameters['thickness'],self.parameters['height']]),
          fusion(self.parameters['position'],[self.parameters['width'],self.parameters['thickness'],0])]
          
        self.faces = [[0,4,5,1],[7,3,2,6],[7,3,0,4],[1,5,6,2]]   
        
    # Draws the faces                
    def draw(self):        
      gl.glPushMatrix()
      gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
      gl.glBegin(gl.GL_QUADS) # Tracé d’un quadrilatère
      gl.glColor3fv(self.parameters['color']) # Couleur gris moyen
       #on trace les faces : GL_FILL
      for i in self.faces:
        gl.glVertex3fv(self.vertices[i[0]])
        gl.glVertex3fv(self.vertices[i[1]])
        gl.glVertex3fv(self.vertices[i[2]])
        gl.glVertex3fv(self.vertices[i[3]])
      gl.glEnd()
      gl.glPopMatrix()


def fusion(list1,list2):
  #deux coordonné entre elle et en donne le résultat
  list=[]
  list.append(list1[0]+list2[0])
  list.append(list1[1]+list2[1])
  list.append(list1[2]+list2[2])
  return list

      
