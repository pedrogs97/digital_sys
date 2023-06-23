import './App.css'
import { Form, FormGroup, Label, Input, Button, Container } from 'reactstrap'
import { useForm } from "react-hook-form"
import axios from 'axios';

function App() {
  const { setValue, handleSubmit } = useForm()
  const api = axios.create({
    baseURL: "http://localhost:8000/api/"
  })

  const submit = (data) => {
    const payload = {
      full_name: data.full_name,
      taxpayer_identification: data.taxpayer_identification,
      loan_value: data.loan_value,
      address: [
        {
          proposal: data.proposal,
          country: data.country,
          state: data.state,
          city: data.city,
          street: data.street,
          number: data.number,
          complement: data.complement,
          zip_code: data.zip_code,
        }
      ]
    }
    api.post('proposal/', payload).then(() => window.alert('Enviado'))
  }
  return (
    <div className="App">
      <Container fluid="sm">
        <Form onSubmit={handleSubmit(submit)}>
          <FormGroup>
            <Label>
              Nome completo
            </Label>
            <Input
              placeholder="Nome completo"
              onChange={(e) => setValue("full_name", e.target.value)}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              CPF
            </Label>
            <Input
              placeholder="CPF"
              onChange={(e) => setValue("taxpayer_identification", e.target.value)}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              Valor
            </Label>
            <Input
              type="number"
              onChange={(e) => setValue("loan_value", Number(e.target.value))}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              País
            </Label>
            <Input
              placeholder="País"
              onChange={(e) => setValue("country", e.target.value)}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              Estado
            </Label>
            <Input
              placeholder="Estado"
              onChange={(e) => setValue("state", e.target.value)}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              Cidade
            </Label>
            <Input
              placeholder="Cidade"
              onChange={(e) => setValue("city", e.target.value)}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              Rua
            </Label>
            <Input
              placeholder="Rua"
              onChange={(e) => setValue("street", e.target.value)}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              Número
            </Label>
            <Input
              type="number"
              onChange={(e) => setValue("number", Number(e.target.value))}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              Complemnto
            </Label>
            <Input
              placeholder="Complemento"
              onChange={(e) => setValue("complement", e.target.value)}
            />
          </FormGroup>
          <FormGroup>
            <Label>
              CEP
            </Label>
            <Input
              placeholder="CEP"
              onChange={(e) => setValue("zip_code", e.target.value)}
            />
          </FormGroup>
          <Button>
            Enviar
          </Button>
        </Form>
      </Container>
    </div>
  )
}

export default App
