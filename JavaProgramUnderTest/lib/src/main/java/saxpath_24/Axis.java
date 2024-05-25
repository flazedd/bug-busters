package saxpath_24;

import java.util.Map;
import java.util.HashMap;

public class Axis
{
    /** Marker for an invalid axis */
    public final static int INVALID_AXIS       =  0;

    /** The <code>child</code> axis */
    public final static int CHILD              =  1;

    /** The <code>descendant</code> axis */
    public final static int DESCENDANT         =  2;

    /** The <code>parent</code> axis */
    public final static int PARENT             =  3;

    /** The <code>ancestor</code> axis */
    public final static int ANCESTOR           =  4;

    /** The <code>following-sibling</code> axis */
    public final static int FOLLOWING_SIBLING  =  5;

    /** The <code>preceding-sibling</code> axis */
    public final static int PRECEDING_SIBLING  =  6;

    /** The <code>following</code> axis */
    public final static int FOLLOWING          =  7;

    /** The <code>preceding</code> axis */
    public final static int PRECEDING          =  8;

    /** The <code>attribute</code> axis */
    public final static int ATTRIBUTE          =  9;

    /** The <code>namespace</code> axis */
    public final static int NAMESPACE          = 10;

    /** The <code>self</code> axis */
    public final static int SELF               = 11;

    /** The <code>descendant-or-self</code> axis */
    public final static int DESCENDANT_OR_SELF = 12;

    /** The <code>ancestor-or-self</code> axis */
    public final static int ANCESTOR_OR_SELF   = 13;

    public static String lookup(int axisNum)
    {
        switch ( axisNum )
        {
            case CHILD:
                return "child";

            case DESCENDANT:
                return "descendant";

            case PARENT:
                return "parent";

            case ANCESTOR:
                return "ancestor";

            case FOLLOWING_SIBLING:
                return "following-sibling";

            case PRECEDING_SIBLING:
                return "preceding-sibling";

            case FOLLOWING:
                return "following";

            case PRECEDING:
                return "preceding";

            case ATTRIBUTE:
                return "attribute";

            case NAMESPACE:
                return "namespace";

            case SELF:
                return "self";

            case DESCENDANT_OR_SELF:
                return "descendant-or-self";

            case ANCESTOR_OR_SELF:
                return "ancestor-or-self";
        }

        return null;
    }

    public static int lookup(String axisName)
    {
        if ( "child".equals( axisName ) )
        {
            return CHILD;
        }

        if ( "descendant".equals( axisName ) )
        {
            return DESCENDANT;
        }

        if ( "parent".equals( axisName ) )
        {
            return PARENT;
        }

        if ( "ancestor".equals( axisName ) )
        {
            return ANCESTOR;
        }

        if ( "following-sibling".equals( axisName ) )
        {
            return FOLLOWING_SIBLING;
        }

        if ( "preceding-sibling".equals( axisName ) )
        {
            return PRECEDING_SIBLING;
        }

        if ( "following".equals( axisName ) )
        {
            return FOLLOWING;
        }

        if ( "preceding".equals( axisName ) )
        {
            return PRECEDING;
        }

        if ( "attribute".equals( axisName ) )
        {
            return ATTRIBUTE;
        }

        if ( "namespace".equals( axisName ) )
        {
            return NAMESPACE;
        }

        if ( "self".equals( axisName ) )
        {
            return SELF;
        }

        if ( "descendant-or-self".equals( axisName ) )
        {
            return DESCENDANT_OR_SELF;
        }

        if ( "ancestor-or-self".equals( axisName ) )
        {
            return ANCESTOR_OR_SELF;
        }

        return INVALID_AXIS;
    }
}
