package battlecry_72;

class bcWord {

    private String word;
    private String phonemes;
    private int syllables;
    private String equalWord;
    private String metricCode;


    public bcWord(String w, String p) {

        word = w;
        phonemes = p;
        metricCode = "";
        syllables = 0;
        equalWord = w;
        parsePhonemes();
    }

    public String getWord() {
        return word;
    }

    public String getPhonemes() {
        return phonemes;
    }

    public int getSyllables() {
        return syllables;
    }

    public String getMetricCode() {
        return metricCode;
    }

    /* setEqualWord()
     * use this to set this word equal with another to prevent them from rhyming
     * (example: "battlecry" should be set equal to "cry", so they don't rhyme)
     */
    public void setEqualWord(String w, String p) {
        //TODO: Get correct metric code
        equalWord = w;
        phonemes = p;
    }

    /* equalTo()
     * check if this word is equal to another.
     */
    public boolean equalTo(String equal) {
        boolean result = false;
        if ((equal.toLowerCase().equals(equalWord.toLowerCase())) ||
                (equal.toLowerCase().equals(word.toLowerCase()))) {
            result = true;
        }
        return result;
    }

    /* parsePhonemes()
     * Searches the phoneme string for valuable information,
     * i.e. syllable count and metric code.
     */
    private void parsePhonemes() {
        String c;
        for (int i = 0; i < phonemes.length(); i++) {
            c = phonemes.substring(i,i+1);
            if ((c.equals("0")) || (c.equals("1")) || (c.equals("2"))) {
                syllables++;
                metricCode += c;
            }
        }
        //if word has only one syllable, mark it with O,I or Z
        //in the generator, these will be handled with extra tolerance
        if (metricCode.equals("0")) {metricCode = "O";}
        else if (metricCode.equals("1")) {metricCode = "I";}
        else if (metricCode.equals("2")) {metricCode = "Z";}
        //most probably, THERE IS NO SUCH THING AS Z
    }

    /* getRhymeKey()
     * Extracts the rhyme key from a phoneme string
     * Set lastSyllableOnly to "true" if you want to check the last syllable only
     * This is important if a longer word should rhyme with a one-syllable word
     */
    public String getRhymeKey(boolean lastSyllableOnly) {
        int syl = syllables;
        if ((syl <= 1) || (lastSyllableOnly)) {syl = 1;}
        else {syl = 2;}
        int i = phonemes.length()-1;
        for (int s = 0; s < syl; s++) {
            while ((i>=0) && (!phonemes.substring(i,i+1).equals("0")) && (!phonemes.substring(i,i+1).equals("1")) && (!phonemes.substring(i,i+1).equals("2"))) {
                i--;
            }
            while ((i>=0) && (!phonemes.substring(i,i+1).equals(" "))) {
                i--;
            }
        }
        return phonemes.substring(i+1);
    }
}
