import React, { Component } from 'react'
import { Card, CardTitle, CardText, Icon } from 'react-mdl'

export default class Hierarchy extends Component {
  componentWillMount() {
    this.props.relay.setVariables({tsn: parseInt(this.props.params.tsn)})
  }

  getSpecies = edge => {
    return (
      <List>
        {edge.node.children.edges.map(edge => {
          return (
            <ListItem key={edge.node.id} style={{display: 'block'}}>
              <span>
                {edge.node.taxonomicUnit.edges[0].node.taxonUnitType.edges[0].node.rankName.trim()}: {edge.node.taxonomicUnit.edges[0].node.completeName}
              </span>
              <span>
                - TSN: {edge.node.tsn}
              </span>
            </ListItem>
          )
        })}
      </List>
    )
  }

  render() {
    if (!this.props.viewer.hierarchies) {
      return <div>Loading...</div>
    }

    return (
      <Card style={{width:'100%'}}>
        <CardTitle>List for Kingdom Animalia</CardTitle>

        <CardText>
          <table style={{width: '100%'}}>
            <tr>
              <th style={{textAlign: 'left'}}>TSN</th>
              <th style={{textAlign: 'left'}}>Name</th>
              <th style={{textAlign: 'left'}}>Credibility Rating</th>
              <th style={{textAlign: 'left'}}>Synonym(s)</th>
            </tr>
            {this.props.viewer.hierarchies.edges.map(edge => {
              return (
                <tr key={edge.node.id}>
                  <td>
                    {edge.node.tsn}
                  </td>
                  <td>
                    {edge.node.taxonomicUnit.edges[0].node.taxonUnitType.edges[0].node.rankName.trim()}:
                    {edge.node.taxonomicUnit.edges[0].node.completeName}
                  </td>
                  <td>
                    {edge.node.taxonomicUnit.edges[0].node.credibilityRtng}
                  </td>
                  <td>
                    
                  </td>
                </tr>
              )
            })}
          </table>
        </CardText>
      </Card>
    )
  }
}
