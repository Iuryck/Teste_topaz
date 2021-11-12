# Teste para Desenvolvedor Python JR

Esse repositório é para o teste de recrutamento para a vaga de Dev Python Jr na empresa Topaz

# Método

Aqui assumi que poderíamos realocar os usuários entre servidores, visto que, caso não fosse possível fazer isso, não haveria muito o que fazer com os usuários. Eles teriam que ser alocados onde caberia, criar mais servidores só aumenta o custo. O código então aloca usuários de acordo com o tempo que falta pro término da execução da tarefa, de forma que os mais próximos de terminar vão estar no mesmo servidor, e logo esse servidor será fechado, assim reduzindo custos.

# Uso

A classe Alocator possui a função **iterating_ticks** que faz tudo que é necessário para cumprir a tarefa

Os testes foram feitos com Unittest
