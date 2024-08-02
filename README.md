# seatBeltDetector
seat belt detector

### README para Aplicação de Detecção de Cinto de Segurança

---

#### Índice
1. [Introdução](#introdução)
2. [Recursos](#recursos)
3. [Instalação](#instalação)
4. [Treinamento](#treinamento)
4. [Uso](#uso)
6. [Dependências](#dependências)
8. [Licença](#licença)

---

### Introdução

A **Aplicação de Detecção de Cinto de Segurança** é uma ferramenta baseada em Python projetada para identificar se motoristas em um conjunto de imagens estão usando cintos de segurança ou não. Dada uma pasta contendo imagens, a aplicação processa cada imagem e gera um relatório indicando quais motoristas estão usando cintos de segurança e quais não estão.

### Recursos

- **Processamento em Lote**: Processa múltiplas imagens em uma única execução.
- **Detecção Precisa**: Utiliza modelos avançados de aprendizado de máquina para garantir alta precisão. (Faltaram dados para um treinamento preciso)
- **Relatórios Detalhados**: Gera um relatório abrangente dos resultados.
- **Fácil de Usar**: Interface de linha de comando simples para interação fácil.

### Instalação

1. **Crie um novo repositório no seu GitHub:**

    Vá até o GitHub e crie um novo repositório para o projeto.

2. **Clone seu repositório:**

    ```sh
    git clone https://github.com/rbiassusi/seatBeltDetector.git
    cd seatBeltDetector
    ```

3. **Crie um ambiente virtual e ative-o:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

4. **Instale as dependências:**

    ```sh
    pip install -r requirements.txt
    ```

### Treinamento
    O modelo contido no repositório contou com uma quantidade pequena de imagens encontradas na internet. Modelo treinando: "cinto_seguranca.model.h5"

1. **Geração da base de treinamento**
    Adicione as imagens na pasta img_trainning dividas em duas subpastas: "com_cinto" e "sem_cinto".

2. **Treinamento**
    Execute o arquivo trainning.py

### Uso
1. **Prepare suas imagens:**
   
   Certifique-se de que todas as imagens estão, a serem analisadas, estejam no diretório: `/img_to_predict`.

2. **Execute a aplicação:**

    ```sh
    python detecta_cintos.py > relatorio.txt
    ```

3. **Revise os resultados:**

    A aplicação irá gerar um relatório chamado `relatorio.txt`, detalhando quais imagens contêm motoristas usando cintos de segurança e quais não.


### Dependências

- Python 3.9+
- OpenCV
- TensorFlow ou PyTorch (dependendo do modelo usado)
- NumPy
- Outras dependências listadas em `requirements.txt`

### Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

Sinta-se à vontade para entrar em contato se tiver alguma dúvida ou precisar de mais assistência.

---

**Informações de Contato**

- **Autor**: Rodrigo Biassusi
- **Email**: rodrigobbiassusi@gmail.com
- **GitHub**: [rodrigobbiassusi@gmail.com](https://github.com/rbiassusi)
