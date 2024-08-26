# Coding an interactive simulation of the PDE Heat Diffusivity Equation of different metals 

This is an intercative code that allows the users to see and experiment with the different conductivities of materials, when exposed to direct heat. It visualizes how thermal energy expands throughout a material from a desired point. 

## Motivation and Background 

This has been my very first project, as well as my first hands-on experience using python. My interets are mainly math and physics and so I wanted to find a way in which I could combine these two interests with coding in particular, which I have started to grow more and more fond of. 
It was suggested to me by my tutor at the immerse summer programm in Cambridge that python was a good way of coding many types of equations. And so I ended up settling for the heat equation. 
I was however, a complete beginner regarding the world of computer science, meaning, as you will see, I had to find a way to not only code an equation, but also make it interactive. 

## Goals and objectives

- Combine a pygame module with the heat equation code to make an interactive visual equation.
- Add to the code, giving it my own features and ideas 
- Start my coding journey with an engaging and meaningful project
- Link a new passion with my interest in physics and math 
- Learn hands-on what it means to code and the difficulties it brings, as well as the joy

## Implementation and Work Process

After dicussing with my tutor, I decided that my task in this project would be to stitch two existing codes together in a way that would allow me to visualize the equation as an interactive module. To do this I used existing code for the PDE Heat Equation and the code for the pygame (_See links for sources)._
After a week of tedious and very intense work of getting down the basics of python in class, I used my newly gained knowledge and through much trial and error I eventually selected the bits of each code I needed to get the two codes to work well together. I faced the biggest challenge when I tried to add the colour function and set it as the temperatures. I eventually overcame the difficulty by defining the color function first individually and then later updating the color according to the heat dissipation as per the heat equation code. 
Once i completed that major obstacle and I had managed to set up the basic code composed of the two base codes, I then wanted to add my own touches to the project, so I could show I had indeed learned and intercted with the code. I decided to first add a touch function which would allow the user to insert the heat anywhere on the material plate and watch it dissipate accross the plane according to the equation. 
Furthermore, I wanted to add different material choices, since I found that only having one choice was rather limiting. I wanted to compare how heat dissipates throughout different materials and how the heat coefficient of each material influences said dissipation. And so I added a dictionary to the code with 6 different materials to choose from. 
This way the user can pick a material out of the list before initiating the simulation. This way the user can compare how different heat coefficients influnce the dissiaption of the same thermal energy. 
Finally, when I showed my work to my tutor, he suggested one final touch. rather than simply adding a touch function to the code, I could also add a dragging function, allowing the user to spread heat evenly throughout the material. 

## Results and Outcome

The code succesfully simulates the dissipation of thermal energy in accordance with the PDE Heat Equation, allowing the user to select a material out of a given list, by dragging or clicking at any desired point. 
I am very happy with how my first coding experince turned out and look forward to more projects. 

## Future Work and Improvements 

Something I would like to improve in the future is the grid. I wish to set it up in a way that doesn´t limit the user to a certain amount of grid points, but rather creates such a detailed grid, that it is seemingless an not noticable. 
This means I would like to find a way to increase the grid resolution without creating unstable coditions for the equation. 
Furthermore, it is important to note that for those who may like to use this code to test different materials from the ones I added in the dictionary, you simply have to add the material directly into the dictionary, along with its corresponding heat coeficient. A quick google search will help you find it. 
However, wehn I was adding the materials I noticed there were certain materials that created unstable conditions for the code. This is somehting else I will try fixing in the future. 

## Conclusion and Reflection 

This project has motivated me to further learn about the interesting world of computer science and has given me the motivation to make new, interesting projects in python and any other programming languages I may learn in the future. 

## Acknowledgments 

I would like to thank my peers in the immerse summer programme, especially those in the computer science lectures. 
I would also like to give a very special thanks to my tutor for the two weeks he patiently spent teaching us and for his help throughout the tedious work process, helping my overcome hurdles I couldnt by myself. 

## References 

- [python - How to make a grid in pygame - Stack Overflow](https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame)
- [Update heat_equation_2d_explicit.py](https://github.com/araujo88/heat-equation-2d/blob/master/heat_equation_2d_explicit.py)
- [Getting pixel color at location with pygame](https://stackoverflow.com/questions/10215803/getting-pixel-color-at-location-with-pygame)
- [Pygame Buttons and Mouse Movement](https://ryanstutorials.net/pygame-tutorial/pygame-buttons.php)
- [Getting position of user click in pygame](https://stackoverflow.com/questions/39626018/getting-position-of-user-click-in-pygame)
- [Code for the Pygame](https://www.pygame.org/docs/)
