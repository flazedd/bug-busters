package tullibee_1;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class Test_Contract_Meta {
@Test
    public void testContractEquals() {
        Contract contract1 = new Contract(1, "AAPL", "STK", "20230615", 165.35, "C", "OPT", "CBOE", "USD", "AAPL", new Vector<>(), "CBOE", false, "", "");
        Contract contract2 = new Contract(1, "AAPL", "STK", "20230615", 165.35, "C", "OPT", "CBOE", "USD", "AAPL", new Vector<>(), "CBOE", false, "", "");
        assertEquals(contract1, contract2);
    }

@Test
    public void testContractNotEquals() {
        Contract contract1 = new Contract(1, "AAPL", "STK", "20230615", 165.35, "C", "OPT", "CBOE", "USD", "AAPL", new Vector<>(), "CBOE", false, "", "");
        Contract contract2 = new Contract(2, "AAPL", "STK", "20230615", 165.35, "C", "OPT", "CBOE", "USD", "AAPL", new Vector<>(), "CBOE", false, "", "");
        assertNotEquals(contract1, contract2);
    }

}