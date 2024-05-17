package jnfe_6;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
public class Test__AbstractNFeAdaptadorBean__Meta_Llama_3_70B_Instruct {
@Test
public void testCalculaDV() {
    assertEquals(3, AbstractNFeAdaptadorBean.calculaDV("3519060511341400010057001000000002546210511"));
}

@Test
public void testCalculaDV2() {
    assertEquals(1, AbstractNFeAdaptadorBean.calculaDV("3519060511341400010057001000000002546210512"));
}

}