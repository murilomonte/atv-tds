// 2) Implemente uma classe chamada “Aluno” que possua atributos para armazenar o
// nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média
// das notas e verificar a situação do aluno (aprovado ou reprovado) de acordo com
// as regras de onde você estuda ou estudou.

class Aluno {
  constructor(nome, matricula, media = 0) {
    this.nome = nome;
    this.matricula = matricula;
    this.media = media;
  }
}                       

const aluno = new Aluno(nome = "Fulano", matricula = "23423s");

console.log(aluno.media);
