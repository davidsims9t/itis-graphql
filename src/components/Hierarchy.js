import React, { Component } from 'react'
import { Card, CardTitle, CardText, Icon } from 'react-mdl'

export default class Hierarchy extends Component {
  componentWillMount() {
    this.props.relay.setVariables({
      tsn: parseInt(this.props.params.tsn),
      level: parseInt(this.props.params.level)
    })
  }

  getSpecies = edge => {
    return edge.node.children.edges.map(edge => {
      return (
        <tr key={edge.node.id}>
          <td style={{width: '25%'}}>
            -- {edge.node.tsn}
          </td>
          <td style={{width: '25%'}}>
            {edge.node.taxonomicUnit.edges[0].node.taxonUnitType.edges[0].node.rankName.trim()}:
            {edge.node.taxonomicUnit.edges[0].node.completeName}
          </td>
          <td style={{width: '25%'}}>
            {edge.node.taxonomicUnit.edges[0].node.credibilityRtng}
          </td>
          <td style={{width: '25%'}}>

          </td>
        </tr>
      )
    })
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
            <thead>
              <tr>
                <th style={{textAlign: 'left', width: '25%'}}>TSN</th>
                <th style={{textAlign: 'left', width: '25%'}}>Name</th>
                <th style={{textAlign: 'left', width: '25%'}}>Credibility Rating</th>
                <th style={{textAlign: 'left', width: '25%'}}>Synonym(s)</th>
              </tr>
            </thead>
            <tbody>
              {this.props.viewer.hierarchies.edges.map(edge => {
                return (
                  <tr key={edge.node.id}>
                    <td colSpan={4}>
                      <table style={{width: '100%'}}>
                        <tbody>
                          <tr>
                            <td style={{width: '25%'}}>
                              {edge.node.tsn}
                            </td>
                            <td style={{width: '25%'}}>
                              {edge.node.taxonomicUnit.edges[0].node.taxonUnitType.edges[0].node.rankName.trim()}:
                              {edge.node.taxonomicUnit.edges[0].node.completeName}
                            </td>
                            <td style={{width: '25%'}}>
                              {edge.node.taxonomicUnit.edges[0].node.credibilityRtng}
                            </td>
                            <td style={{width: '25%'}}>

                            </td>
                          </tr>
                          {this.getSpecies(edge)}
                        </tbody>
                      </table>
                    </td>
                  </tr>
                )
              })}
            </tbody>
          </table>
        </CardText>
      </Card>
    )
  }
}
