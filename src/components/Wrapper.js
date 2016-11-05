import React, { Component } from 'react'
import { Layout, Content, Header } from 'react-mdl'

export default class extends Component {
  render() {
    return (
      <Layout fixedHeader={true}>
        <Header>
          ITIS
        </Header>

        <Content style={{padding: 20}}>
          {this.props.children}
        </Content>
      </Layout>
    )
  }
}
