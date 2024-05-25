package openjms_66;

import java.util.Hashtable;
import java.util.Vector;

public class CommandLine {

    /**
     * A list of option of switches on the command line. A switch
     * is either set or not
     */
    private Vector _switches = new Vector();

    /**
     * A dictionary of all the options and their associated values
     */
    private Hashtable _options = new Hashtable();

    /**
     * Construct an instance of this class with the specified string
     * array.
     *
     * @param       args        command line argument
     */
    public CommandLine(String[] args) {
        processCommandLine(args);
    }

    /**
     * Default constructor which simply initialised the class
     */
    public CommandLine() {
    }

    /**
     * Check if the following option or command has been specified
     *
     * @param       name        name of option or command
     * @return      boolean     true if it has been specified
     */
    public boolean exists(String name) {
        return _switches.contains(name) || _options.containsKey(name);
    }

    /**
     * Check if the following option has been specified.
     *
     * @param       name        name of the option
     * @return      boolean     true if it has been specified
     */
    public boolean isSwitch(String name) {
        return _switches.contains(name);
    }

    /**
     * Check if the following parameter has been specified.
     *
     * @param       name        name of the parameter
     * @return      boolean     true if it has been specified
     */
    public boolean isParameter(String name) {
        return _options.containsKey(name);
    }

    /**
     * Return the value of the parameter or option. If the string nominates
     * an option then return null
     *
     * @param       name        name of option or parameter
     * @return      String      value of parameter or null
     */
    public String value(String name) {
        String result = null;

        if (_options.containsKey(name)) {
            result = (String) _options.get(name);
        }

        return result;
    }

    /**
     * Return the value of the parameter or option, returning a default
     * value if none is specified
     *
     * @param       name        name of option or parameter
     * @param       defaultValue the default value
     * @return      String      value of parameter
     */
    public String value(String name, String defaultValue) {
        String result = value(name);
        return (result != null) ? result : defaultValue;
    }

    /**
     * Add the following option or parameter to the list. An option will
     * have a null value, whereas a parameter will have a non-null value.
     * <p>
     * This will automatically overwrite the previous value, if one has been
     * specified.
     *
     * @param       name        name of option or parameter
     * @param       value       value of name
     * @return      boolean     true if it was successfully added
     */
    public boolean add(String name, String value) {
        return add(name, value, true);
    }

    /**
     * Add the following option or parameter to the list. An option will
     * have a null value, whereas a parameter will have a non-null value.
     * <p>
     * If the overwrite flag is true then this value will overwrite the
     * previous value. If the overwrite flag is false and the name already
     * exists then it will not overwrite it and the function will return
     * false. In all other circumstances it will return true.
     *
     * @param       name        name of option or parameter
     * @param       value       value of name
     * @param       overwrite   true to overwrite previous value
     * @return      boolean     true if it was successfully added
     */
    public boolean add(String name, String value, boolean overwrite) {
        boolean result = false;

        if (value == null) {
            // it is an option
            if ((_switches.contains(name)) &&
                    (overwrite)) {
                _switches.addElement(name);
                result = true;
            } else if (!_switches.contains(name)) {
                _switches.addElement(name);
                result = true;
            }
        } else {
            // parameter
            if ((_options.containsKey(name)) &&
                    (overwrite)) {
                _options.put(name, value);
                result = true;
            } else if (!_options.containsKey(name)) {
                _options.put(name, value);
                result = true;
            }
        }

        return result;
    }

    /**
     * This method processes the command line and extracts the list of
     * options and command lines. It doesn't intepret the meaning of the
     * entities, which is left to the application.
     *
     * @param       args        command line as a collection of tokens
     */
    private void processCommandLine(String[] args) {
        boolean prev_was_hyphen = false;
        String prev_key = null;

        for (int index = 0; index < args.length; index++) {
            if (args[index].startsWith("-")) {
                // if the previous string started with a hyphen then
                // it was an option store store it, without the hyphen
                // in the _switches vector. Otherwise if the previous was
                // not a hyphen then store key and value in the _options
                // hashtable
                if (prev_was_hyphen) {
                    add(prev_key, null);
                }

                prev_key = args[index].substring(1);
                prev_was_hyphen = true;

                // check to see whether it is the last element in the
                // arg list. If it is then assume it is an option and
                // break the processing
                if (index == args.length - 1) {
                    add(prev_key, null);
                    break;
                }
            } else {
                // it does not start with a hyphen. If the prev_key is
                // not null then set the value to the prev_value.
                if (prev_key != null) {
                    add(prev_key, args[index]);
                    prev_key = null;
                }
                prev_was_hyphen = false;
            }
        }
    }

}

