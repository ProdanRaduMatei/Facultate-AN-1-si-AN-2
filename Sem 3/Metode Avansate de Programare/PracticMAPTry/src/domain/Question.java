package domain;

public class Question implements Identifiable<Integer> {
    private Integer id;
    private String text;
    private String answer;
    private Integer score;
    private String usranswr;

    private Boolean isAnswered = false;

    public Question(Integer id, String text, String answer, Integer score, String usranswr) {
        this.id = id;
        this.text = text;
        this.answer = answer;
        this.score = score;
        this.usranswr = usranswr;
    }

    @Override
    public Integer getId() {
        return id;
    }

    @Override
    public void setId(Integer id) {
        this.id = id;
    }

    public String printQuestion(){
        return "Question{" +
                "id=" + id +
                ", text='" + text + '\'' +
                ", answer='" + answer + '\'' +
                ", score=" + score +
                ", usranswr=" + usranswr +
                '}';
    }

    public String getText() {
        return text;
    }

    public String getAnswer() {
        return answer;
    }

    public Integer getScore() {
        return score;
    }

    public String getUsranswr() {
        return usranswr;
    }

    public Boolean getIsAnswered() {
        return isAnswered;
    }

    public void setIsAnswered(Boolean isAnswered) {
        this.isAnswered = isAnswered;
    }
}
