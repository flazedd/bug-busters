package corina_35;

import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.InvocationTargetException;

import java.util.Comparator;
import java.util.Collections;
import java.util.List;

public class Sort {
    // this class should never be instantiated
    private Sort() { }

    /** Sort a list from lowest to highest.
     @param data a list to sort
     @param field the field of the Objects in data to sort by
     */
    public static void sort(List data, String field) throws IllegalArgumentException {
        sort(data, field, false);
    }

    /** Sort a list.
     @param data a list to sort
     @param field the field of the Objects in data to sort by
     @param decreasing if true, sort highest-to-lowest; else, lowest-to-highest
     */
    public static void sort(List data, String field, boolean decreasing) throws IllegalArgumentException {
        // no data -> no need to sort (and also no way to try,
        // since i don't even know what type it would be)
        if (data.size() == 0)
            return;

        Class c = data.get(0).getClass();

        try {
            // possible bug: if data contains different classes of objects, data[0].class
            // might be the declarer of field |field| -- do i need to call
            // -- f = f.getDeclaringClass().getDeclaredField(field)?
            Field f = c.getDeclaredField(field);

            // see if data[0].field is visible
            try {
                f.get(data.get(0));

                // if it passes that, then f is visible to me.
                // so sort by the field.
                sortByField(data, f, decreasing);

            } catch (IllegalAccessException iae) {

                // well, we can't see field |field|.  what else can we try?
                // we try a get<field>() method, of course!

                String methodName = makeAccessorName(field);

                try {
                    Method m = c.getMethod(methodName, new Class[] { });
                    // FIXME: what if this fails?

                    sortByMethod(data, m, decreasing);

                } catch (NoSuchMethodException nsme) {
                    // no get() method exists, abort
                    throw new IllegalArgumentException("No method '" + methodName + "()' exists " +
                            "in class " + c.getName() + "!");
                }

            }
        } catch (NoSuchFieldException nsfe) {
            throw new IllegalArgumentException("No such field '" + field + " exists " +
                    "in class " + c.getName() + "!");
        }
    }

    // given a field, return the name of its accessor.
    // e.g., "myField" => "getMyField"
    private static String makeAccessorName(String field) {
        return "get" +
                Character.toUpperCase(field.charAt(0)) +
                field.substring(1);
    }

    // sort |data| by |field|, high-to-low iff |decreasing|.
    private static void sortByField(List data, Field field, boolean decreasing) throws IllegalArgumentException {
        final boolean reverse = decreasing;
        final Field f = field;

        Collections.sort(data, new Comparator() {
            public int compare(Object o1, Object o2) {
                try {
                    Comparable v1 = (Comparable) f.get(o1);
                    Comparable v2 = (Comparable) f.get(o2);

                    if (v1 == null && v2 == null) return 0;
                    if (v1 == null) return (reverse ? +1 : -1);
                    if (v2 == null) return (reverse ? -1 : +1);

                    int x = v1.compareTo(v2);
                    return (reverse ? -x : x);
                } catch (IllegalAccessException iae) {
                    // gah, nothing i can do here.
                    // can't happen.  or, rather, almost can't happen.
                    throw new IllegalArgumentException("No access to field '" + f.getName() + "()'");
                    // an IAE can be thrown here (doesn't need to be declared), and it'll clear to the top.
                }
            }
        });
    }

    // sort |data| by result of |method|, high-to-low iff |decreasing|
    private static void sortByMethod(List data, Method method, boolean decreasing) throws IllegalArgumentException {
        final boolean reverse = decreasing;
        final Method m = method;

        Collections.sort(data, new Comparator() {
            public int compare(Object o1, Object o2) {
                try {
                    Comparable v1 = (Comparable) m.invoke(o1, new Object[] { });
                    Comparable v2 = (Comparable) m.invoke(o2, new Object[] { });

                    if (v1 == null && v2 == null) return 0;
                    if (v1 == null) return (reverse ? +1 : -1);
                    if (v2 == null) return (reverse ? -1 : +1);

                    int x = v1.compareTo(v2);
                    return (reverse ? -x : x);
                } catch (IllegalAccessException iae) {
                    // gah, nothing i can do here.
                    // can't happen.  or, rather, almost can't happen.
                    throw new IllegalArgumentException("No access to method '" + m.getName() + "()'");
                } catch (InvocationTargetException ie) {
                    throw new IllegalArgumentException("Error invoking method '" + m.getName() + "()'");
                }
            }
        });
    }
}
