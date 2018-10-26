import java.io.File;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;

import java.util.*;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class App {
	
	
	
	public static void main(String[] args) {
		
		String text =  "Mix water and cornmeal and bring to the boiling point in a heavy-based saucepan.\r\n" + 
				"Cook 5 minutes.\r\n" + 
				"Beat eggs well and add with other materials to the mush.\r\n" + 
				"Beat well and bake in a well-greased pan for 25 minutes in a hot oven.\r\n" + 
				"Serve from the same dish with a spoon.";
				
				/* another example recipe for test. Example data is taken from wikihow.com
				"Preheat oven to 375 degrees F. Grease a 9 x 13-inch baking pan.\r\n" + 
				"Cream butter, brown sugar, granulated sugar and then add egg yolks.\r\n" + 
				"Beat mixture well.\r\n" + 
				"Add the boiling water, cocoa and baking soda in a separate mixing bowl.\r\n" + 
				"Mix together.\r\n" + 
				"Add to batter in bowl.\r\n" + 
				"Add vanilla then beat well.\r\n" + 
				"Add baking powder and then flour.\r\n" + 
				"Beat well.\r\n" + 
				"Add egg whites and beat well.\r\n" + 
				"Bake 30 to 35 minutes or until cake tests done.\r\n" + 
				"Frost as desired.\r\n" + 
				"Makes 1 large cake.\r\n";
		*/
		String path = "";  //enter the file path for your directory
        String food = path+ "food.xml";
 	     String container = path+ "containers.xml";
	      String measure = path+ "Measure_volume.xml";
	      String fluid = path+ "Cause_fluidic_motion.xml";
	      String changephase = path+ "Change_of_phase.xml";
       
	      String verbs = path+"verbs.txt";
	      
	       associateFrames(food, text);     
	      associateFrames(container, text);    
	      associateFrames(measure, text); 
	      associateFrames(fluid, text);   
	      associateFrames(changephase, text); 
	    
	   
	    ArrayList<String> list= createVerbList(verbs);
	    for (int counter = 0; counter < list.size(); counter++) { 		      
	      String x= getSentence(text,list.get(counter)); 
	      if(x!=null)
	      {
	    	  String arr[] = x.split(" ", 2);

	    	  String firstWord = arr[0];
	      if(firstWord.toLowerCase().contains(list.get(counter)))
	     System.out.println("Sentence:"+ x + "\n"+"action:"+list.get(counter));
	    }   		
	    
	    }
	   
	    identifyDuration(text);
	    
	   }


public static void associateFrames(String filepath, String text)
{
	  try {
	 File inputFile = new File(filepath);
     DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
     DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
     Document doc = dBuilder.parse(inputFile);
     doc.getDocumentElement().normalize();
  //   System.out.println("Root element :" + doc.getDocumentElement().getNodeName());
     NodeList nList = doc.getElementsByTagName("lexUnit");
     //System.out.println("----------------------------");
     String filename= inputFile.getName();
    

     for (int temp = 0; temp < nList.getLength(); temp++) {
        Node nNode = nList.item(temp);
   //     System.out.println("\nCurrent Element :" + nNode.getNodeName());
        
        if (nNode.getNodeType() == Node.ELEMENT_NODE) {
           Element eElement = (Element) nNode;
           
           if(eElement.getAttribute("name").endsWith(".n") || eElement.getAttribute("name").endsWith(".v")) {
        	   
        	   eElement.getAttribute("name").replaceAll(".n", " ");
        	   eElement.getAttribute("name").replaceAll(".v", " ");
           }
      String a=  getSentence(text, eElement.getAttribute("name").replaceAll(".n", " "));
	       if (a!=null) {
	    	   System.out.println("sentence:: " + a + "\nframe: " + filename.replaceAll(".xml",  " ") + "\nword: " +  eElement.getAttribute("name")+"\n");
            
	       }
        }
     }
  } catch (Exception e) {
     e.printStackTrace();
  }
}



private static  Pattern END_OF_SENTENCE = Pattern.compile("\\.\\s+");

public static String getSentence(String text, String word) {
     String lcword = word.toLowerCase();
    return END_OF_SENTENCE.splitAsStream(text)
            .filter(s -> s.toLowerCase().contains(lcword))
            .findAny()
            .orElse(null);
}
	
public static ArrayList<String> createVerbList (String filename)
{
	ArrayList<String> verbList = new ArrayList<String>();
   try {
            File f = new File(filename);

            BufferedReader b = new BufferedReader(new FileReader(f));

            String readLine = "";

            while ((readLine = b.readLine()) != null) {
                verbList.add(readLine);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
   return verbList;
    }

public static void  identifyDuration (String text) {
	
	String timesentence= getSentence(text,"minutes");
    tagTime(timesentence);
	
}

public static boolean isNum(String x)
{
	 boolean numeric = true;

     numeric = x.matches("-?\\d+(\\.\\d+)?");

     if(numeric)
         return true;
     else
        return false;
 }


public static void tagTime(String sentence)
{
	String[] words = sentence.split(" ");
	for(int i=0; i<words.length; i++)
	{
		if(isNum(words[i]))
		{
			System.out.println("sentence:" + sentence + "\nduration:"+ words[i]+" "+ words[i+1]);
		}
			
	}
}


}
