package a4j_2;


import java.io.Serializable;
import java.util.ArrayList;
public class Directors implements Serializable {

    ArrayList directors;

    public String[] getDirector() {
        String[] retString = new String[directors.size()];
        if (directors.size() > 0) directors.toArray(retString);

        return retString;
    }

    public void setDirector(String[] newString) {
        directors = new ArrayList(newString.length);
        for (int i = 0; i < newString.length; i++) {
            directors.add(newString[i]);
        }

    }

    public ArrayList getDirectorsArray() {
        return directors;
    }

    public String getDirector(int index) {
        String retString = null;

        if (directors.size() - 1 < index) {
            retString = (String) directors.get(index);
        }

        return retString;
    }

    public String toString() {
        StringBuffer output = new StringBuffer();
        String string = new String();
        if (directors != null && directors.size() > 0) {
            output.append("# of Directors = " + directors.size() + "\n");
            for (int x = 0; x < directors.size(); x++) {
                string = directors.get(x).toString();
                if (string != null) {
                    output.append("Director - " + string + "\n");
                }
            }
        } else {
            output.append("Director is null or size 0" + "\n");
        }
        return output.toString();
    }

}
