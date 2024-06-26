package tullibee_1;

public class __UnderComp {

    public int    m_conId;
    public double m_delta;
    public double m_price;

    public __UnderComp() {
        m_conId = 0;
        m_delta = 0;
        m_price = 0;
    }

    public boolean equals(Object p_other) {

        if (this == p_other) {
            return true;
        }

        if (p_other == null || !(p_other instanceof __UnderComp)) {
            return false;
        }

        __UnderComp l_theOther = (__UnderComp)p_other;

        if (m_conId != l_theOther.m_conId) {
            return false;
        }
        if (m_delta != l_theOther.m_delta) {
            return false;
        }
        if (m_price != l_theOther.m_price) {
            return false;
        }

        return true;
    }
}

