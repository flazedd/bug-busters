package lagoon_52;

/**
 * Some utility methods. All methods in this class are static.
 */
public final class Utils
{
    /**
     * Private default constructor to prevent instantiation.
     */
    private Utils() {}


    /**
     * Encode a path name or URL into a filename.
     *
     * The encoding function is not intended to be inversible.
     */
    public static String encodePath(String path)
    {
        StringBuffer sb = new StringBuffer(path.length());

        for (int i = 0; i < path.length(); i++)
        {
            char c = path.charAt(i);
            switch (c)
            {
                case '-':
                    sb.append("--");
                    break;
                case '_':
                    sb.append("__");
                    break;
                case '$':
                    sb.append("$$");
                    break;
                case '~':
                    sb.append("~~");
                    break;

                case '/':
                    sb.append('-');
                    break;
                case '\\':
                    sb.append('-');
                    break;
                case '*':
                    sb.append('_');
                    break;
                case '?':
                    sb.append('$');
                    break;
                case ':':
                    sb.append('~');
                    break;
                default:
                    sb.append(c);
            }
        }

        return sb.toString();
    }


    /**
     * Encode a path name or URL into a Java identifier.
     *
     * The encoding function is not intended to be inversible.
     */
    public static String encodePathAsIdentifier(String path)
    {
        StringBuffer sb = new StringBuffer(path.length());

        char c = path.charAt(0);
        if (Character.isJavaIdentifierStart(c))
            sb.append(c);
        else
            sb.append("_"+((int)c)+"_");

        for (int i = 1; i < path.length(); i++)
        {
            c = path.charAt(i);
            if (Character.isJavaIdentifierPart(c))
                sb.append(c);
            else
                sb.append("_"+((int)c)+"_");
        }

        return sb.toString();
    }



    /**
     * Check whether an URL is absolute.
     * Returns true if the URL contains at least one colon, and
     * the first colon is before the first slash (if any).
     */
    public static boolean absoluteURL(String url)
    {
        int colon = url.indexOf(':');
        if (colon < 0) return false;

        int slash = url.indexOf('/');
        if (slash < 0) return true;

        return colon < slash;
    }


    /**
     * Check whether an URL is pseudo-absolute.
     * Returns true if the URL start with a slash.
     */
    public static boolean pseudoAbsoluteURL(String url)
    {
        return (url.length() > 0) && (url.charAt(0) == '/');
    }


    /**
     * Generate a {@link java.lang.String} with a specified number
     * of a given character.
     */
    public static String nChars(int n, char c)
    {
        StringBuffer sb = new StringBuffer(n);
        for (int i = 0; i<n; i++)
            sb.append(c);
        return sb.toString();
    }

}
