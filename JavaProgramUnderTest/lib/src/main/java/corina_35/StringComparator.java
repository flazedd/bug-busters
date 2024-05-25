package corina_35;

import java.util.Comparator;
import java.text.Collator;

public class StringComparator implements Comparator {

    /**
     The compare method used by Comparator.  Simply calls
     <pre>
     return compare((String) o1, (String) o2);
     </pre>

     @param o1 the first string to compare
     @param o2 the second string to compare
     @return the result of their comparison
     */
    public int compare(Object o1, Object o2) {
        return compare((String) o1, (String) o2);
    }

    /**
     Compare two strings using voodoo.

     @param s1 the first string
     @param s2 the second string
     @return -1, 0, or +1, if the first string is less than, equal
     to, or greater than the second string
     */
    public static int compare(String s1, String s2) {
        // PERF: extract this?
        // this collator is a comparator that will ignore case, accents
        Collator collator = Collator.getInstance();
        collator.setStrength(Collator.PRIMARY);

        // BETTER: wrap natural sort around this?

        // ALSO: maybe CollatorKeys would yield better perf.  investigate.

        // task: compare name1, s2
        for (int i=0; i<s1.length(); i++) {
            // s2 shorter: return +1
            if (s2.length() <= i)
                return +1;

            // compare chars s1[i], s2[i]:

            // first, make them into strings: unfortunately,
            // collator only compares strings, not chars,
            // so make some 1-character strings.
            String str1 = s1.substring(i, i+1);
            String str2 = s2.substring(i, i+1);

            // try comparing, ignoring case and accents.
            // this will put "J" before "K", for instance,
            // but "C" and "c" and "C," will all sort the same.
            int test = collator.compare(str1, str2);
            if (test != 0)
                return test;

            // now compare again, ignoring case, but not accents.
            // this will put "C" and "c" together, but separate
            // out "C,", which will go after all C's.
            test = str1.compareToIgnoreCase(str2);
            if (test != 0)
                return test;
        }

        // s2 longer
        if (s2.length() > s1.length())
            return -1;

        // same
        return 0;
    }
}

