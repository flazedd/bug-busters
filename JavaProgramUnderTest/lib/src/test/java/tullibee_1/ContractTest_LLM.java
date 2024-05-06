package tullibee_1;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Vector;
public class ContractTest_LLM {
@Test
void testClone() throws CloneNotSupportedException {
    Contract contract = new Contract(1, "symbol", "secType", "expiry", 1.0, "right", "multiplier", "exchange", "currency", "localSymbol", new Vector(), "primaryExch", false, "secIdType", "secId");
    Contract clone = (Contract) contract.clone();
    assertEquals(contract, clone);
}

}